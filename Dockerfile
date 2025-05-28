<<<<<<< HEAD
# Use official Python base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

# Expose port 5000 (Flask default)
EXPOSE 5000

# Run the Flask app on 0.0.0.0 to accept external connections
CMD ["python", "app2.py"]
>>>>>>> 7abf9c17a92c06a5bb5b735f9bb70616b299e5fb
