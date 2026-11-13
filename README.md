# Жұмыс орындарын ұсыну жүйесі (Курстық жұмыс)

SQLite + Python + GitHub Pages сайты. SQL сұраныстар браузерде `sql.js` арқылы орындалады.

## PyCharm-да іске қосу
1. `File → Open` → осы папканы таңдаңыз.
2. `main.py` ашып Run басыңыз: `docs/vacancies.db` және `docs/queries.json` жасалады.
3. Сайтты жергілікті көру: Run Configuration-ға `--serve` параметрін қосыңыз (немесе терминалда `python main.py --serve`).

## GitHub Pages
1. PyCharm: `Git → Create Git Repository`, коммит жасаңыз, `Git → GitHub → Share Project on GitHub`.
2. GitHub-та репозиторий → Settings → Pages → Source: `Deploy from a branch`, Branch: `main`, папка `/docs` → Save.
3. 1-2 минуттан кейін сайт `https://<логин>.github.io/<репозиторий>/` мекенжайында ашылады.
