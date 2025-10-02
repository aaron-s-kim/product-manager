# Product Manager (Django)
Simple Django app for managing products with categories and tags.

## Tech Stack
- Python 3.12
- Django 5.2.X
- PostgreSQL

## Setup
1. Create virtual environment & activate
```sh
python -m venv .venv
source .venv/bin/activate
```
2. Install packages
```sh
# Install prerequisites for postgresql
sudo apt install libpq-dev
# Install django & PostgreSQL DB adapter
pip install django django-environ psycopg2-binary
```

3. Environment setup
Copy `.env.example` to `.env`, update with own values, and generate a new SECRET_KEY

4. Setup Database
```sh
# Make sure PostgreSQL is running, and DB exists
python manage.py migrate
```

5. Run server
```sh
python manage.py runserver
```
Visit `http://localhost:8000/`

