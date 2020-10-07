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
[View CoreyMs Tutorial](https://www.youtube.com/watch?v=qDwdMDQ8oX4)
- Templates allow you to return more complex HTML than what is initialized in our `views.py` file.
- Create a subdirectory to organize templates (Django convention).
- example: blog -> templates -> blog -> template.html
- `apps.py` contains a `BlogConfig` class that needs to be added in the `INSTALLED_APPS` list in `settings.py` as `'blog.apps.BlogConfig'`.
- Change `views.py` to load template(s) by using the Django Shortcuts module.
- Template Inheritance:
    - `base.html` makes code DRY
    - `home.html` and `about.html` both use `base.html` because they only differ in a small way. 

## Styling:
- used bootstrap starter template code in `base.html`
- CSS belongs in `static directory`
- blog -> static -> blog -> `main.css`
- load static files
    - first line in `base.html`
    - ` <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}" `
- `base.html` imports `main.css`

## Navigation Bar:
- In `base.html`, there is a navigation bar with links to Home, About, Login, and Register.
- Currently hard-coded, we can change to be more dynamic.
- ` <a class="nav-item nav-link" href="{% url 'blog-home' %}">Home</a> `
- `blog-home` references `urlpatterns` in `urls.py`

## Django Administration:
[View CoreyMS Tutorial](https://www.youtube.com/watch?v=1PkNiYlkkjo)
- create database, auth_user and create superuser
    - `python3 manage.py migrate`: runs migrations, makes auth_user table
    - `python3 manage.py createsuperuser`: create superuser username/email/password
    - Run server again to reload admin page. Log in with superuser.
        - ability to create new users/permissions. 

## Databases and Migration
[View CoreyMS Tutorial](https://www.youtube.com/watch?v=aHC3uTkT9r8)
- Django already created a `models.py` file in each app directory. 
- Create database as class, specify fields.
- `python3 manage.py makemigrations`: checks for changes
- creates migration file in migrations folder
- `python3 manage.py sqlmigrate blog 0001`: generates SQL code for database
- `python3 manage.py migrate` run migration
- `python3 manage.py shell`: interactive console
    - test: `from blog.models import Post`
    - `from django.contrib.auth.models import User`
    - `User.objects.all()`
    - returns a QuerySet
    - `User.objects.filter(username='ReaganBarrington')`
        - `user = User.objects.filter(username='ReaganBarrington').first()`: captures in variable.
        - `user.id` or `user.pk` returns id/primary key
        ### Creating a new Post for a User:
        - `post_1 = Post(title='Blog 1', content='First Post Content!', author=user)`
         - `post_1.save()`
        - `Post.objects.all()`
        - `exit()`
        ### Get all Posts that User Created:
        - `User.post_set` now can run queries
        - `user.post_set.all()`: get QuerySet for posts by user
        - `user.post_set.create(title='Blog 3', content='Third Post Content!')`: create new post and authomatically save to database
        - `Post.objects.all()`
        ### Viewing the new Post DB in Admin Page:
        - `admin.py` in blog directory
        - Register model:
            - import model: `from .models import Post`
            - `admin.site.register(Post)` 
        - Now within admin page, you can update/delete

## User Registration
[View CoreyMS Tutorial](https://www.youtube.com/watch?v=q4jPR-M0TAQ)
- Create a new app: users `python3 manage.py startapp users`
- Add app to `INSTALLED_APP`
- Create register function in `views.py`
    - User creation form already exists in Django. A class that will be turned to HTML. 
    - `from django.contrib.auth.forms import UserCreationForm`
- Create new template (`register.html`). `<form>` needs `method="POST"` and a token.
    - as_p
    - GET and POST: insert a conditional that if there's a post request, validate the form, if a get, just render page. 
- `from django.contrib import messages`
    - `messages.debug`
    - `messages.info`
    - `messages.success`
    - `messages.warning`
    - `messages.error`
- need a new form to inherit from default UserCreationForm because we want to add a new field: email.
- `crispy_forms` for styling

## Login/Logout
[View CoreyMS Tutorial](https://www.youtube.com/watch?v=3aVqWaLjqS4)
- Login/Logout Views are included with Django:
    - `from django.contrib.auth import views as auth_views` 
    - `path('login/', auth_views.LoginView.as_view, name='login'),`
    - `path('logout/', auth_views.LogoutView.as_view, name='logout'),`
- Create a login template in users directory. Pass in `template_name` as argument in `urlpattern` so Django knows where to locate template.
- Link to different components by `href="{% url 'login' %}`
- NOTE: by default, successful login will try to navigate to the path: `/accounts/profile/`. In `settings.py` you can create new `LOGIN_REDIRECT_URL`
- Django includes `is_authenticated`
    ### RESTRICTING ROUTES:
    - Django provides a Login Required decorator
    - `from django.contrib.auth.decorators import login_required`
    - add `LOGIN_URL` to `settings.py` if not using default.

## User Profile and Picture
[View CoreyMS Tutorial](https://www.youtube.com/watch?v=FdVuKt_iuSI)
- `models.py` in users app, extend default model
- migrations: 
    - `pip install Pillow`
    - `python3 manage.py makemigrations`
    - run migrations: `python3 manage.py migrate`
    - `admin.py` in users app - register model
- Generates a `profile_pics` directory





