from flask import Flask

app = Flask(__name__)  # Flask app instance named 'app'

# Define your routes here
@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
