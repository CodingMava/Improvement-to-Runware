# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirement parameters directly to optimize layer caching
RUN pip install --no-cache-dir flask flask-cors supabase

# Copy the backend code into the container
COPY app.py .

# Expose the API port
EXPOSE 5000

# Run the Flask gateway binding to all network interfaces
CMD ["python", "app.py"]