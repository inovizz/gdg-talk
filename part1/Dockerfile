# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update
RUN apt-get install mysql-server -y

RUN pip install -r requirements.txt

RUN mysql -u root -p pass < db_setup.sql

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]