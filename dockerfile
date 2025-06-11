FROM python:3.11-slim        # Use a lightweight Python 3.11 base image
WORKDIR /app                 # Set working directory inside the container to /app
COPY requirements.txt .      # Copy requirements.txt into the container
RUN pip install -r requirements.txt  # Install all Python dependencies
COPY . .                    # Copy all project files into the container
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]  # Start the server using gunicorn
