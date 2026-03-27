# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code 
COPY app/ .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
