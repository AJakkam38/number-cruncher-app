# Base image
FROM python:3.8-slim-buster

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

# Set up work directory
WORKDIR /app

# Copy the current 'flask' directory contents into the container at /app 
ADD . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the command to start uWSGI server
CMD ["uwsgi", "app.ini"]