# Blog Website

A professional Django-powered blog application for publishing articles, managing users, and showcasing posts with a modern web interface.

## Features

- User authentication (login, logout, registration)
- Create, edit, and delete blog posts
- List all posts on the homepage
- View post details
- Responsive design with custom CSS
- SQLite database for development
- Admin interface for managing content
- Automated tests for models and views

## Project Structure

```
blog_website/
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── __init__.py
│       └── 0001_initial.py
├── django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
├── static/
│   └── css/
│       └── base.css
├── templates/
│   ├── base.html
│   ├── home.html
│   └── post_detail.html
├── requirement.txt
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rishukumark19/blog_website.git
   cd blog_website
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the site:**
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Running Tests

To run automated tests:
```bash
python manage.py test
```

## Customization
- Update `static/css/base.css` for your own styles.
- Edit templates in the `templates/` folder for custom layouts.
- Add new models or views in the `blog/` app as needed.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.

## Author
Rishu Kumar

---
For any questions or support, please contact [rishukumark19](https://github.com/rishukumark19).
