# quickstart-django-api

QuickStartAPI

## Technologies Stack.

- **Language**: [https://www.python.org/](https://www.python.org/)
- **Web Framework**: [https://www.djangoproject.com/](https://www.djangoproject.com/)
- **Api Rest Framework**: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
- **Database**: [https://www.postgresql.org/](https://www.postgresql.org/)
- **Application Monitoring**: [https://sentry.io/](https://sentry.io/)

## Features

## Getting Started

Ensure you have installed the following:

- Git
- Python 3.10.4
- PostgreSQL 14

### Part One: Terminal commands

Clone the repo:

```bash
git clone https://git.jambopay.co.ke/ochazima/quickstart-django-api.git
```

Change directory

```
cd quickstart-django-api
```

### Part Two: Terminal commands

Enter the postgres Shell:

```bash
sudo -u postgres -i psql
```

Create the database and user as ypu wish to use:

```bash
CREATE DATABASE quickstart-django-api;
```

Create the user:

```bash
CREATE USER quickstart-django-api WITH PASSWORD 'quickstart-django-api';
```

Grant the user access to the database:

```bash
GRANT ALL PRIVILEGES ON DATABASE quickstart-django-api TO quickstart-django-api;
```

Create a .env file under root project directory following the template in example.env

### Part Three: Termial commands (Project Setup)

Create virtualenv:

```
python3 -m venv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install the requirements

```
pip3 install --upgrade pip

pip3 install -r requirements.txt
```

Run the migrations for postgres

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```

Run the Application

```
python3 manage.py runserver
```

Run the application: PRODUCTION Mode

```
gunicorn manage:app --worker-class gevent --bind 127.0.0.1:5000 --log-level info
```

### Part Four: Termial commands (Celery Worker Setup)

On a new terminal window activate the preinstalled virtual environment:

```
source venv/bin/activate
```

Start the celery workers with command:

```
celery -A QuickStartAPI worker -l info
```

### Part Five: Termial commands (Flower Celery Worker Monitor Tool)

On a new terminal window activate the preinstalled virtual environment:

```
source venv/bin/activate
```

Start the flower monitor with command:

```
celery -A QuickStartAPI flower --port=5566 -E
```

Endpoints Documentation are accessible at \*\*http://127.0.0.1:8000/

## Used Packages

- celery==5.2.7
- Django==4.1.5
- django-debug-toolbar==3.6.0
- django-environ==0.9.0
- django-filter==22.1
- django-cors-headers==3.13.0
- djangorestframework==3.14.0
- djangorestframework_simplejwt==5.2.2
- django-redis==5.2.0
- drf-yasg==1.21.4
- flower==1.2.0
- psycopg2-binary==2.9.5
- pytest==7.2.0
- pytest-cov==4.0.0
- pytest-django==4.5.2
- requests==2.28.1
- sentry-sdk==1.12.1

## Documentation

To generate the code documentation run:

```
make html
```

You can find the html file to open under docs/build/html/index.html

## License

Copyright (c) 2022, [Outhan Chazima](https://github.com/outhan-chazima).
