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
# Install packages into virtual env
pip install -r requirements.txt
```

3. Environment setup
Copy `.env.example` to `.env`, update with own values, and generate a new SECRET_KEY

4. Setup Database, create & run migrations, then seed
- Make sure PostgreSQL is running, and DB exists
```sh
# Create migrations
python manage.py makemigrations
# Apply migrations  
python manage.py migrate
# Seed database
python manage.py seed_db
```

5. Run server
```sh
python manage.py runserver
```
Visit `http://localhost:8000/`

## Additional Notes
- Use `DEBUG=Flase` in prod
- Generate a unique SECRET_KEY for prod
