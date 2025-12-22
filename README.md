# Cybersecurity project 1 report

## Installation instructions

1. Install Django: `pip install django`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Open browser to `http://127.0.0.1:8000/`
5. (Optional) To create user do: python manage.py createsuperuser
---

## FLAW 1: Cross-Site Scripting (XSS) - A03:2021

**Where:** `todos/templates/todos/index.html`

**Description:**
The template uses the `|safe` filter when rendering todo text, disabling Django's protection which allows JS injection.

**How to fix:**
Remove the `|safe` filter in `todos/templates/todos/index.html`.

---

## FLAW 2: Cross-Site Request Forgery (CSRF)

**Where:** `todos/views.py` (`add`) and `todos/templates/todos/index.html`

**Description:**
The `add` view uses `@csrf_exempt` and the form does not have `{% csrf_token %}`, disabling CSRF protections.

**How to fix:**
1. Remove `@csrf_exempt` from the `add` view in `todos/views.py`.
2. Add `{% csrf_token %}` inside the form in `todos/templates/todos/index.html`.

---

## FLAW 3: Broken Access Control - Missing Authentication - A01:2021

**Where:** `todos/views.py` (`index`) and `todos/models.py`

**Description:**
The app saves todos publicly: there is no per-user access.

**How to fix:**
- Add a `ForeignKey` to `User` on the `Todo` model in `todos/models.py`.
- Do migration: `python manage.py makemigrations todos` and `python manage.py migrate`.
- In `todos/views.py` require login and filter todos: `todos = Todo.objects.filter(user=request.user)`.

---

## FLAW 4: Insecure Direct Object Reference (IDOR) - A01:2021

**Where:** `todos/views.py` (`delete` and `toggle`)

**Description:**
`delete` and `toggle` accessed todos by ID without checking ownership.

**How to fix:**
Require authentication and fetch objects of the current user:
```
if not request.user.is_authenticated:
    return redirect('login')
todo = Todo.objects.get(id=todo_id, user=request.user)
```

---

## FLAW 5: Security Misconfiguration - A05:2021

**Source:** `security_helsinki/settings.py`

**Description:**
`DEBUG = True` and `ALLOWED_HOSTS = []` are insecure in production.

**How to fix:**
1. Set `DEBUG = False` in production.
2. Configure `ALLOWED_HOSTS` with your hostnames (e.g., `['domain.com']`).
