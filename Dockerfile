# Use the official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project into the container
COPY . ./app/
# Collect static files
# RUN python manage.py collectstatic --noinput
# # Run Django server
# CMD ["gunicorn", "inventory_management.wsgi:application", "--bind", "0.0.0.0:8000"]
# Expose the application port
EXPOSE 8000
# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
RUN pip install coverage
