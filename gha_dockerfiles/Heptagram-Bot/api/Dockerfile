# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
LABEL org.opencontainers.image.source https://github.com/heptagram-bot/api

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

# Set pip to have no saved cache
ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# setup poetry
COPY pyproject.toml poetry.lock ./
RUN pip3 install poetry
RUN poetry install

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Transfer source to image
COPY . .

# Run api
CMD [ "uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000" ]
