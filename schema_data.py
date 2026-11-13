SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE Users (user_id INTEGER PRIMARY KEY, full_name TEXT NOT NULL, email TEXT, phone TEXT, city TEXT, experience_years INTEGER);
CREATE TABLE Companies (company_id INTEGER PRIMARY KEY, company_name TEXT NOT NULL, industry TEXT, city TEXT, email TEXT);
CREATE TABLE Vacancies (vacancy_id INTEGER PRIMARY KEY, company_id INTEGER, title TEXT NOT NULL, description TEXT, city TEXT, salary REAL, experience_years INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id));
CREATE TABLE Skills (skill_id INTEGER PRIMARY KEY, skill_name TEXT NOT NULL, category TEXT);
CREATE TABLE User_Skills (user_id INTEGER, skill_id INTEGER, skill_level TEXT, PRIMARY KEY (user_id, skill_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id), FOREIGN KEY (skill_id) REFERENCES Skills(skill_id));
CREATE TABLE Vacancy_Skills (vacancy_id INTEGER, skill_id INTEGER, required_level TEXT, PRIMARY KEY (vacancy_id, skill_id),
    FOREIGN KEY (vacancy_id) REFERENCES Vacancies(vacancy_id), FOREIGN KEY (skill_id) REFERENCES Skills(skill_id));
CREATE TABLE Applications (application_id INTEGER PRIMARY KEY, user_id INTEGER, vacancy_id INTEGER, application_date TEXT, status TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id), FOREIGN KEY (vacancy_id) REFERENCES Vacancies(vacancy_id));
"""

DATA = {
    "Users": [
        (1, 'Айдана Сәрсенова', 'aidana@mail.kz', '+77010000001', 'Астана', 1),
        (2, 'Әлихан Нұрланов', 'alikhan@mail.kz', '+77010000002', 'Алматы', 2),
        (3, 'Мадина Ермекова', 'madina@mail.kz', '+77010000003', 'Астана', 0),
        (4, 'Данияр Ахметов', 'daniyar@mail.kz', '+77010000004', 'Қарағанды', 3),
        (5, 'Аружан Қасымова', 'aruzhan@mail.kz', '+77010000005', 'Астана', 1),
        (6, 'Нұрсұлтан Әлиев', 'nursultan@mail.kz', '+77010000006', 'Шымкент', 2),
        (7, 'Әсем Мұратова', 'asem@mail.kz', '+77010000007', 'Алматы', 1),
        (8, 'Ержан Беков', 'erzhan@mail.kz', '+77010000008', 'Астана', 4),
        (9, 'Динара Омарова', 'dinara@mail.kz', '+77010000009', 'Қарағанды', 0),
        (10, 'Тимур Қайратов', 'timur@mail.kz', '+77010000010', 'Шымкент', 2)],
    "Companies": [
        (1, 'Astana IT Solutions', 'IT', 'Астана', 'info@astanait.kz'),
        (2, 'Digital Kazakhstan', 'IT', 'Алматы', 'hr@digital.kz'),
        (3, 'FinTech Group', 'Қаржы', 'Астана', 'jobs@fintech.kz'),
        (4, 'Smart Education', 'Білім беру', 'Қарағанды', 'hr@smartedu.kz'),
        (5, 'TechnoPark', 'IT', 'Шымкент', 'info@technopark.kz'),
        (6, 'DataLab', 'Деректерді талдау', 'Алматы', 'hr@datalab.kz'),
        (7, 'AI Future', 'Жасанды интеллект', 'Астана', 'jobs@aifuture.kz'),
        (8, 'Web Solutions', 'IT', 'Қарағанды', 'info@websolutions.kz'),
        (9, 'Smart Finance', 'Қаржы', 'Алматы', 'hr@smartfinance.kz'),
        (10, 'EduTech KZ', 'Білім беру', 'Шымкент', 'info@edutech.kz')],
    "Vacancies": [
        (1, 1, 'Python Developer', 'Python тілінде бағдарламалау', 'Астана', 450000, 1),
        (2, 2, 'Data Analyst', 'Деректерді талдау', 'Алматы', 400000, 1),
        (3, 3, 'Data Scientist', 'Жасанды интеллект және деректер', 'Астана', 600000, 2),
        (4, 4, 'Junior SQL Developer', 'SQL және деректер базасы', 'Қарағанды', 300000, 0),
        (5, 5, 'Web Developer', 'Веб-сайттарды әзірлеу', 'Шымкент', 380000, 1),
        (6, 6, 'Machine Learning Engineer', 'Машиналық оқыту модельдері', 'Алматы', 650000, 2),
        (7, 7, 'AI Engineer', 'Жасанды интеллект жүйелері', 'Астана', 700000, 3),
        (8, 8, 'Database Administrator', 'Деректер базасын басқару', 'Қарағанды', 420000, 2),
        (9, 9, 'Financial Analyst', 'Қаржылық деректерді талдау', 'Алматы', 500000, 1),
        (10, 10, 'IT Support Specialist', 'ІТ жүйелеріне қолдау көрсету', 'Шымкент', 280000, 0)],
    "Skills": [
        (1, 'Python', 'Бағдарламалау'), (2, 'SQL', 'Деректер базасы'),
        (3, 'Machine Learning', 'Жасанды интеллект'), (4, 'Data Analysis', 'Деректерді талдау'),
        (5, 'Communication', 'Жеке дағдылар'), (6, 'Java', 'Бағдарламалау'),
        (7, 'C++', 'Бағдарламалау'), (8, 'Statistics', 'Математика'),
        (9, 'HTML/CSS', 'Веб әзірлеу'), (10, 'Excel', 'Деректерді талдау')],
    "User_Skills": [
        (1, 1, 'Орта'), (1, 2, 'Бастапқы'), (2, 1, 'Жоғары'), (2, 3, 'Орта'), (3, 2, 'Бастапқы'),
        (3, 4, 'Орта'), (4, 1, 'Жоғары'), (4, 3, 'Жоғары'), (5, 5, 'Жоғары'), (6, 6, 'Орта')],
    "Vacancy_Skills": [
        (1, 1, 'Орта'), (1, 2, 'Бастапқы'), (2, 2, 'Орта'), (2, 4, 'Орта'), (3, 1, 'Жоғары'),
        (3, 3, 'Жоғары'), (4, 2, 'Бастапқы'), (5, 1, 'Орта'), (6, 3, 'Жоғары'), (7, 1, 'Жоғары')],
    "Applications": [
        (1, 1, 1, '2026-09-01', 'Қаралуда'), (2, 1, 2, '2026-09-03', 'Қабылданды'),
        (3, 2, 3, '2026-09-04', 'Қаралуда'), (4, 3, 4, '2026-09-06', 'Қабылданды'),
        (5, 4, 3, '2026-09-07', 'Қабылданбады'), (6, 5, 5, '2026-09-08', 'Қаралуда'),
        (7, 6, 6, '2026-09-09', 'Қаралуда'), (8, 7, 7, '2026-09-10', 'Қабылданды'),
        (9, 8, 8, '2026-09-11', 'Қаралуда'), (10, 9, 9, '2026-09-12', 'Қабылданбады')],
}
