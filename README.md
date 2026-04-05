# Full-Stack-Django5-TailwindCSS-HTMX
Full Stack Web Development with Django 5, TailwindCSS, HTMX

* NOTE: although the course taught `django v5`, this repo used `django v6.0.3`, look for `pyproject.toml` for more about packages & dependencies.
* Create the project environment:
    ```bash
    uv init --name DjangoBlog --no-package --no-workspace --vcs none
    uv add django
    uv venv --prompt DjProject
    uv sync --all-packages
    uv lock
    ```
* Building & Running Docker Container:
    1. `docker build -t djangoblog .`
    2. `docker run --rm -p 8005:8000 --name djangoblog djangoblog`
        * Run Docker Container with Volumes: `docker run --rm -p 8005:8000 --name djangoblog -v "$(pwd):/code" djangoblog`
    3. `docker exec djangoblog uv run manage.py makemigrations`
        * `docker exec djangoblog uv run manage.py migrate`

- Adding translations:
    - `$ docker exec djangoblog uv run manage.py makemessages  --locale=uz `
    - `$ docker exec djangoblog uv run manage.py compilemessages`
- Docker compose commands:
    - Completely recreate the docker image: `docker compose up --build --force-recreate --no-deps <service_name>`
---

## Django Course Notes:

* Architecture of the Django Framework: ![django-architecture](django-mvt.png)
* Starting/Creating a new django project: **`$ uv run django-admin startproject <projectname> . `**
* To start the application: **`$ uv run manage.py runserver`**
    * *Ctrl+C* to stop the server.
* Run & apply migrations: **`$ uv run manage.py migrate`**
* Create a superuser: **`$ uv run manage.py createsuperuser`**
* Access the admin panel: `/admin` (http://127.0.0.1:8000/admin)
* Create django app: **`$ uv run manage.py startapp <appname>`**
* Create migrations (for db): **`$ uv run manage.py makemigrations`**
* Create custom migration: **`$ uv run manage.py makemigrations --empty <appname>`**
* Django automatically escapes the HTML content, we can turn it off in templates using `{{ content | safe }}`.
* Django has built-in command `check --deploy` for security checks: **`uv run manage.py check --deploy`**
*
---
* **Browser Cookie** (a.k.a. HTTP cookie) -- a small block of data created by a web server while a user is browsing a website and placed on the user's computer or other device by the user's web browser. \
https://en.wikipedia.org/wiki/HTTP_cookie
* **CSRF** (Cross-Site Request Forgery / **XSRF**) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. \
https://owasp.org/www-community/attacks/csrf \
https://en.wikipedia.org/wiki/Cross-site_request_forgery
* `POST`, `PUT` and `DELETE` methods are known as "unsafe", which means we should use CSRF protection on them. Other methods are "safe".
* Preventing CSRF attack:
    1. CSRF tokens -- server-generated secret code that must be present in the form.
    2. SameSite cookies -- cookies are not sent from third party sites on form submissions. (This is now default in most browsers)
*
