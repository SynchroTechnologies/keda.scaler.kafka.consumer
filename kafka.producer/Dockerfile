# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified with apt
RUN pip install --no-cache-dir kafka-python six

# Run consumer.py when the container launches
CMD ["python", "producer.py"]
