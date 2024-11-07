# Django Jinja Project

This project is a simple web application built using Django and Jinja templating engine. The application includes pages like Home, About Us, and Contact Us, styled with CSS.

## Features

- **Home Page**: Displays the main content of the website.
- **About Us Page**: Information about the Java class.
- **Contact Us Page**: Provides contact information and a form for inquiries.

## Project Structure

The project structure is as follows:

```
djangoJinja/
├── JinjaProject/
│   ├── db.sqlite3             # SQLite database
│   ├── manage.py              # Django management script
│   ├── JinjaApp/
│   │   ├── __init__.py        # Package initialization file
│   │   ├── admin.py           # Admin configurations
│   │   ├── apps.py            # App configuration
│   │   ├── static/
│   │   │   └── css/           # CSS files for styling
│   │   ├── templates/
│   │   │   ├── home.html      # Home page template
│   │   │   ├── base.html      # Base template
│   │   │   ├── about.html     # About Us page template
│   │   │   └── contact.html   # Contact Us page template
│   │   ├── migrations/
│   │   │   └── __init__.py    # Migration file for database schema
│   │   ├── models.py          # Database models
│   │   ├── tests.py           # Unit tests for the app
│   │   ├── views.py           # Views for rendering templates
│   │   └── urls.py            # URL routing for the app
│   └── JinjaProject/
│       ├── __init__.py        # Package initialization file
│       ├── settings.py        # Django settings configuration
│       ├── urls.py            # Root URL routing
│       ├── asgi.py            # ASGI configuration
│       └── wsgi.py            # WSGI configuration
├── jinja_env/                 # Virtual environment folder
│   ├── Include/
│   ├── Lib/
│   └── Scripts/
├── requirements.txt  
└── .gitignore                 # Git ignore file
```

## Requirements

- Python 3.x
- Django 3.x or higher
- SQLite (used as the default database)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/OumaCavin/djangoJinja.git
```

### 2. Set Up Virtual Environment

Create and activate a virtual environment to install dependencies:

1. Create a virtual environment:

    ```bash
    python -m venv jinja_env
    ```

2. Activate the virtual environment:

   - For Windows:

     ```bash
     .\jinja_env\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source jinja_env/bin/activate
     ```

### 3. Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can manually install Django:

```bash
pip install django
```

### 4. Apply Migrations

Apply the database migrations:

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 6. Access the Application

Open your web browser and go to:

```
http://127.0.0.1:8000
```

## File Structure

- `manage.py`: Django management script used to run commands such as migrations and development server.
- `JinjaProject/settings.py`: Settings configuration for the Django project.
- `JinjaProject/urls.py`: Root URL configuration.
- `JinjaApp/`: Application folder containing templates, static files, models, views, and other app-related files.

## Templates

- `home.html`: Template for the home page.
- `base.html`: Base template used across the website.
- `about.html`: Template for the About Us page.
- `contact.html`: Template for the Contact Us page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
