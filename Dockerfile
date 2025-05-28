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
