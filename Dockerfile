# Use official Python image
FROM python:3.9-slim

# Set work directory inside container
WORKDIR /app

# Copy all files to /app
COPY . .

# Install Flask
RUN pip install Flask

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

