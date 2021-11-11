# Dockerfile for creating the Web Manager server

# WARNING: This Dockerfile is not suitable for production use.

# Based on:
# - https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.8.dockerfile
# - https://medium.com/@harpalsahota/dockerizing-python-poetry-applications-1aa3acb76287

FROM python:3.9

WORKDIR /web-manager

EXPOSE 80

# Copy all the required content.
COPY saltapi saltapi
COPY poetry.lock .
COPY pyproject.toml .

# Install
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN ${HOME}/.poetry/bin/poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
CMD uvicorn --port 80 --host 0.0.0.0 saltapi.main:app
