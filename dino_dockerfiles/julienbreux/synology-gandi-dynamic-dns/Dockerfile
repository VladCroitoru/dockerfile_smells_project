##
# NAME             : julienbreux/synology-gandi-dynamic-dns
# VERSION          : 1
# DOCKER-VERSION   : 1.11
# DESCRIPTION      : Synology Gandi dynamic DNS updater.
# DEPENDENCY       : none
# TO_BUILD         : docker build --pull=true --no-cache --rm -t julienbreux/synology-gandi-dynamic-dns:latest .
# TO_SHIP          : docker push julienbreux/synology-gandi-dynamic-dns:latest
# TO_RUN           : docker run -ti --rm julienbreux/synology-gandi-dynamic-dns:latest
##

FROM python:3-slim

MAINTAINER Julien Breux <julien.breux@gmail.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]
