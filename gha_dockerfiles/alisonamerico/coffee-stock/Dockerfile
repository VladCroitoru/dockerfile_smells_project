# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create folder
RUN mkdir /code

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/