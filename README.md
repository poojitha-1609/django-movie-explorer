# Django Movie Explorer

A clean Django web application for exploring popular Indian movies, their lead actors, genres, and languages.

## Features

- Responsive movie explorer homepage
- Individual detail pages for each movie
- Django URL routing and function-based views
- Reusable HTML templates
- Custom CSS styling
- SQLite database configuration for local development

## Movies Included

Baahubali, Pushpa, RRR, Salaar, KGF, Vikram, Leo, Jailer, Devara, and Kalki 2898 AD.

## Requirements

- Python 3.10 or newer
- Django 6.1 or compatible version

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install django
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project Structure

- `movies/views.py` contains the movie views.
- `movies/urls.py` contains URL routes.
- `movies/templates/` contains the HTML templates.
- `movies/templates/static/css/` contains the stylesheet.

## License

This project is intended for educational and portfolio use.
