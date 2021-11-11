FROM python:2-alpine

MAINTAINER Sullivan SENECHAL <soullivaneuh@gmail.com>

RUN apk add --no-cache --virtual .deps libffi \
&& apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev \
&& pip install nagios-api diesel greenlet \
&& apk del .build-deps

RUN mkdir -p /opt/nagios/var && touch /opt/nagios/var/status.dat

EXPOSE 8080

CMD ["nagios-api", "-p", "8080", "-s", "/opt/nagios/var/status.dat"]
