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
- Remember to put secret in a git-ignored .env file
- create new `url.py` file in new app's directory
    - `urlpatterns` hold path names. `/admin` routes to `admin.site.urls` as default. `/blog` utilizes `include` function to search for matching path name in `blog.urls` 's `urlpatterns`.

## Templates:
- Templates allow you to return more complex HTML than what is initialized in our `views.py` file.
- Create a subdirectory to organize templates (Django convention).
- example: blog -> templates -> blog -> template.html
- `apps.py` contains a `BlogConfig` class that needs to be added in the `INSTALLED_APPS` list in `settings.py` as `'blog.apps.BlogConfig'`.
- Change `views.py` to load template(s) by using the Django Shortcuts module.
- Template Inheritance:
    - `base.html` makes code DRY
    - 
