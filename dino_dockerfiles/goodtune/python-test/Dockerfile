FROM python:3
MAINTAINER Gary Reynolds <gary@touch.asn.au>

RUN apt-get update && apt-get install -y \
  libpython2.7-dev \
  postgresql-client-9.4 \
  && rm -rf /var/lib/apt/lists/*

COPY run-tests.py /usr/local/bin/run-tests

RUN curl -s https://bootstrap.pypa.io/get-pip.py | python2.7

COPY requirements.txt /tmp/requirements.txt
RUN pip2.7 install --no-cache-dir -r /tmp/requirements.txt

VOLUME /src
WORKDIR /src

ENV TOXWORKDIR /tmp/.tox
