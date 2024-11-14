# portfolio_project/run.py

from app import create_app
import webbrowser
from threading import Timer

app = create_app()

def open_browser():
    """Open the default web browser on the localhost."""
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    app.run(debug=True)
    # Start a timer to open the browser after Flask starts
    Timer(1, open_browser).start()
    app.run()