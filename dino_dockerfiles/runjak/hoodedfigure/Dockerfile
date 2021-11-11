FROM alpine:latest

MAINTAINER Jakob Runge <sicarius@g4t3.de>

RUN apk update \
 && apk add git python3-dev py-pip \
 && rm /var/cache/apk/APKINDEX*tar.gz

RUN git clone https://github.com/runjak/hoodedfigure /srv/hoodedfigure

WORKDIR /srv/hoodedfigure

RUN pip install --upgrade pip \
 && pip install -r /srv/hoodedfigure/REQUIREMENTS

ENTRYPOINT python /srv/hoodedfigure/main.py
