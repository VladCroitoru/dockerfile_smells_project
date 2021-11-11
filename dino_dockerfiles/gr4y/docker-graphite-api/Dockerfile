FROM ubuntu:xenial
MAINTAINER Sascha Wessel <swessel@gr4yweb.de>

# Update System
RUN apt-get update -y && apt-get upgrade -y

# Install Dependencies
RUN apt-get install -y build-essential python-dev libffi-dev libcairo2-dev python-pip

# Install pip dependencies
RUN pip install gunicorn graphite-api[sentry,cyanite]

# Add Config file
ADD graphite-api.yaml /etc/graphite-api.yaml

# Expose Port
EXPOSE 8000

VOLUME /data/graphite

CMD gunicorn -b 0.0.0.0:8000 -w 2 --log-level debug graphite_api.app:app