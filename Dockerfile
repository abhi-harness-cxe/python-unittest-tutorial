# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application
COPY app.py .
RUN mkdir /harness && echo "Hello World" >> test.txt

# Expose port 5000
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
