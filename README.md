# Django 1.9 simple site

## Requirements
Django 1.9.2

Only for PosgtreSQL database server: `pip install psycopg2`

## Installation
- Postgresql: `brew install postgresql` on **Mac** or `sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib` on **Ubuntu**.

## Setup Postgresql

Login in Ubuntu/Linux shell with *postgres* user by: `sudo su - postgres`, tnan `psql`

#### *On Mac OS*:
To have launchd start postgresql at login:

  `ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents`
  
Then to load postgresql now:

  `launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist`
  
Or, if you don't want/need launchctl, you can just run:

  `postgres -D /usr/local/var/postgres`

##### Postgresql shell setup
On Linux just use postgresl shell (`psql`) and commands on maner `your-login-name=#` as described below, **but on Mac**:
`psql -d template1 `, in opened shell type `createdb` command and ENTER, and than use commands in postgresql shell (`psql`):

```
your-login-name=# CREATE DATABASE catssite;
CREATE DATABASE
your-login-name=# CREATE USER catadmin WITH PASSWORD '1234';
CREATE ROLE
your-login-name=# ALTER ROLE catadmin SET client_encoding TO 'utf8';
ALTER ROLE
your-login-name=# GRANT ALL PRIVILEGES ON DATABASE catssite TO catadmin;
GRANT
```


## Setup Django 1.9 SQL tables
If you just want use sqlite one-file database engine replace in settings.py:

```
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cats-billing.sqlite'),
```

Run in Terminal

```
python manage.py migrate
```
#### Creating an admin user for /admin on site
```
python manage.py createsuperuser
```

#### Start the development server

```
python manage.py runserver
```

