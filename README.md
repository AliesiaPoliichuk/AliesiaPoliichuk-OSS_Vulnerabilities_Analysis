# OSS_Vulnerabilities_Analysis

Проєкт із аналізу даних про кібервразливості (Common Vulnerabilities and Exposures), який включає:

- Очистку та підготовку даних
- Завантаження до бази PostgreSQL
- Візуалізацію в Google Looker Studio

## 📁 Структура

- `scripts/` — Python-скрипти для обробки та експорту даних
- `cve_data_new.sql` — SQL-запити для аналітики та графіків
- `resources/` — (опційно) CSV-файли, якщо публічні
- `README.md` — опис проєкту

## 🧪 Дашборд у Looker Studio

📊 [Переглянути дашборд](https://lookerstudio.google.com/reporting/3f477e93-84b8-4f53-828e-471d9127a3a5)

Він включає:
- Тренд кількості вразливостей по роках
- Найвразливіші продукти
- Частоти категорій вразливостей (CWE)

## 🛠️ Технології

- Python (Pandas, SQLAlchemy)
- PostgreSQL
- Google Looker Studio
