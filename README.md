# Portfolio Project

This repository contains a personal portfolio built with **Flask**. It showcases projects, experience and skills in a clean, responsive interface.

## Features
- Bootswatch Darkly theme based on Bootstrap&nbsp;5
- Font Awesome icons for improved navigation
- Pages for About, Experience, Projects, Skills and Contact
- Contact form with basic validation and flash messages
- Ready for deployment with Gunicorn via the `Procfile`

## Requirements
- Python 3.10+
- See `requirements.txt` for Python dependencies

## Running locally
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Visit `http://localhost` in your browser.

## Deployment
The application can be deployed to any platform that supports Flask. On Heroku-like platforms, the included `Procfile` runs the app using Gunicorn:

```text
web: gunicorn app:app
```

Feel free to customize the templates and static files to make it your own!
