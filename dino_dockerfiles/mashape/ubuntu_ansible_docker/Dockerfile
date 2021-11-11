FROM williamyeh/ansible:ubuntu14.04

RUN apt-get update && \
  apt-get install -y \
  python-pip curl python-virtualenv python-distutils-extra \
  python-apt libcurl4-openssl-dev python-dev libffi-dev libssl-dev

COPY requirements.txt /

RUN pip install -r requirements.txt
