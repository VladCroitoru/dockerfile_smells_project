FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV DEBUG False
ENV APP_ROOT /code

WORKDIR ${APP_ROOT}

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
  locales \
  locales-all \
  build-essential \
  libpq-dev \
  libjpeg-dev \
  binutils \
  libproj-dev \
  gdal-bin \
  libxml2-dev \
  libxslt1-dev \
  zlib1g-dev \
  libffi-dev \
  libssl-dev \
  curl \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get clean --dry-run

COPY ./app ${APP_ROOT}
