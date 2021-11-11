FROM ubuntu:14.04

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y \
      build-essential \
      git \
      nginx \
      supervisor \
      libffi-dev \
      libpq-dev \
      libssl-dev \
      python \
      python-dev \
      python-setuptools \
      python-pip \
      python-virtualenv

RUN pip install supervisor-stdout

# We manage these via supervisor.
RUN service supervisor stop
RUN service nginx stop
