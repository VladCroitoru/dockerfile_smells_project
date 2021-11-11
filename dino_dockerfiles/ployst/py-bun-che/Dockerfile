FROM ubuntu:14.04.4

# Basic package setup
RUN apt-get update && apt-get install -y \
    apache2 \
    libapache2-mod-wsgi-py3 \
    libpq-dev \
    python3.4 \
    python3-pip \
    python3-psycopg2

RUN pip3 install -U psycopg2
RUN a2enmod wsgi

# Make python point to python3
RUN ln -s /usr/bin/python3 /usr/local/bin/python

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
