# Use an official Ruby runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8080
EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--log-level", "info", "app:app"]
