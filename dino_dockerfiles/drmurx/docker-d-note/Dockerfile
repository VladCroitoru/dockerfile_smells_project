FROM alpine:3.5
MAINTAINER Jan Kunzmann <jan-docker@phobia.de>

RUN apk add --no-cache python2 py2-flask py2-crypto py-setuptools uwsgi uwsgi-python git \
 && git clone https://github.com/atoponce/d-note.git /build \
 && cd /build \
 && python setup.py install \
 && cd / \
 && rm -rf build \
 && apk del git

COPY config/d-note.ini /etc/dnote/
COPY script/uwsgi-http-dnote.sh /usr/local/bin/

ENV APPLICATION_ROOT=/
ENV PROCESSES=1
ENV THREADS=2

VOLUME /dnote
EXPOSE 8080

CMD [ "/usr/local/bin/uwsgi-http-dnote.sh" ]
