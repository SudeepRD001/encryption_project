# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file if it exists
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy the entire project
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run Django with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "encryption_project.wsgi:application"]
