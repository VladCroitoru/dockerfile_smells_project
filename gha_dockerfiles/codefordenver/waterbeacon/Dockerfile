# pull official base image
FROM python:3.6

# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# prevents python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1

# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pathlib
RUN pip install -r /app/requirements.txt
RUN apt-get update
RUN apt-get install -y nano
RUN apt-get install -y binutils libproj-dev gdal-bin
