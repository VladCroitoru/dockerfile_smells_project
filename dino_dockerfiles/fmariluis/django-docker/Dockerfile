FROM python:3.5.1

MAINTAINER Franco Mariluis <fmariluis@gmail.com>

# Installing gettext for i18n support
RUN apt-get update \
      && apt-get install -y --no-install-recommends \
      gettext \
      && rm -rf /var/lib/apt/lists/*

COPY base.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
