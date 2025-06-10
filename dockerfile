# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the app with Gunicorn
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:80"]
