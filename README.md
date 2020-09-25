# Learning Django

## Initializing:
- `django-admin startproject project_name`
- Files generated:
    - `manage.py` : allows for command line commands
    - `project.name`
        - `__init__.py` : informs python that this is a package
        - `settings.py` : configurations
        - `urls.py` : set up mapping/routing
        - `wsgi.py` : communications with web server (/admin already set up)

- `python3 manage.py runserver` localhost:8000

## Getting Started:
- a single project contains multiple apps (ex: blog, store, etc).
- `python3 manage.py startapp app_name`
- Files generated:
    - `__init__.py`
    - `admin.py`
    - `apps.py`
    - `migrations`
    - `models.py`
    - `tests.py`
    - `views.py`
        - `from django.http import HttpResponse`
- create new `url.py` file in new app's directory