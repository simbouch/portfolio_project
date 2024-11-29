from app import create_app

app = create_app()  # Ensure the `create_app` function exists and initializes the Flask app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)  # Bind to all network interfaces on port 8000
