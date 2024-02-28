# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code into the container
COPY . .

# Install Flask
RUN pip install --no-cache-dir Flask gunicorn

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the Flask application with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
