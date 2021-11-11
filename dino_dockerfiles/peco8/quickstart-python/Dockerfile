# Using official Python runtime base image
FROM python:2.7-slim

MAINTAINER "Toshiki Inami <t-inami@arukas.io>"

# Set the applilcation directory
ENV APP_HOME /app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Get pip to download and install requirements:
COPY requirements.txt $APP_HOME/
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
COPY . $APP_HOME

# Make port 5000 available for publish
EXPOSE 80

# Start server
CMD python $APP_HOME/server.py
