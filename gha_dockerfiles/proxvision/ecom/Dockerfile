# Gets you python installed on slim, nice and easy
FROM python:3.8.12-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Switch to whatever dir you want your app to be installed in
WORKDIR /code

# Copy only the pyproject and lock file in for now, 
# This way you don't have to re-install deps when just your code changes
COPY pyproject.toml poetry.lock /code/

# Update pip and apt-get and pip install poetry
RUN pip install -U pip \
    && apt-get update \
    && pip install poetry

# Install from your poetry lock file in
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi 
# Copy in all your stuff
COPY . /code/