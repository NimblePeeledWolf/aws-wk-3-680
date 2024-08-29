# Use a specific Python version
FROM python:3.10.12-slim

# Update and install curl
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose port 5001 for the Flask application
EXPOSE 5000


RUN useradd -m appuser
USER appuser

ENV PORT=5000

CMD gunicorn --workers=3 --bind 0.0.0.0:$PORT app:app

