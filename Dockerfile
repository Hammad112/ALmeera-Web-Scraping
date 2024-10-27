# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary Python packages
RUN pip install --no-cache-dir requests beautifulsoup4

# Run the Python script
CMD ["python", "./main_scrap.py"]
