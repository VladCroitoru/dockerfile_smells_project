# Dockerfile

# Pull base image
FROM python:3.8.5-buster

# python
# Set environment variables
ENV PYTHONUNBUFFERED 1
# prevents python creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 

# pip
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# poetry
# https://python-poetry.org/docs/configuration/#using-environment-variables
ENV POETRY_VERSION=1.0.9
ENV POETRY_VIRTUALENVS_CREATE=false
# make poetry create the virtual environment in the project's root
# it gets named `.venv`
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
# do not ask any interactive question
ENV POETRY_NO_INTERACTION=1

# Install environment dependencies
RUN apt-get update && apt-get -y install apt-utils binutils libgdal-dev gdal-bin libproj-dev gcc

# create folder
RUN mkdir /code

# Set work directory
WORKDIR /code

# Install dependencies
RUN python -m pip install --upgrade pip
RUN pip install poetry
COPY pyproject.toml poetry.lock /code/
RUN poetry install

# Copy project
COPY . /code/
