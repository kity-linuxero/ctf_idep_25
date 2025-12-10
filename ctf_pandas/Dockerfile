# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local directory contents to the container at /app
COPY . .

# Install the necessary packages
RUN pip install Flask gunicorn

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run the command to start the Gunicorn server
# It will serve the 'application' object from the 'main' module (main.py)
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:application"]
