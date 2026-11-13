"""Дерекқорды құрады (SQLite) және docs/ ішіндегі сайтқа қажетті файлдарды жасайды.
   python main.py          -> docs/vacancies.db + docs/queries.json
   python main.py --serve  -> жергілікті сервер http://localhost:8000
"""
import http.server, json, pathlib, socketserver, sqlite3, sys, webbrowser
from queries import QUERIES
from schema_data import DATA, SCHEMA

DOCS = pathlib.Path(__file__).parent / "docs"


def build():
    DOCS.mkdir(exist_ok=True)
    path = DOCS / "vacancies.db"
    path.unlink(missing_ok=True)
    conn = sqlite3.connect(path)
    conn.executescript(SCHEMA)
    for table, rows in DATA.items():
        conn.executemany(f"INSERT INTO {table} VALUES ({','.join('?' * len(rows[0]))})", rows)
    conn.commit()
    print("Деректер базасы құрылды:", path)
    out = []
    for title, sql, note in QUERIES:  # әр сұранысты тексеру
        rows = conn.execute(sql).fetchall()
        print(f"  OK  {title:<24} {len(rows)} жол")
        out.append({"title": title, "sql": sql, "note": note})
    (DOCS / "queries.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    conn.close()


def serve(port=8000):
    handler = lambda *a, **k: http.server.SimpleHTTPRequestHandler(*a, directory=str(DOCS), **k)
    with socketserver.TCPServer(("", port), handler) as srv:
        webbrowser.open(f"http://localhost:{port}")
        print(f"Сервер: http://localhost:{port}  (тоқтату: Ctrl+C)")
        srv.serve_forever()


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
