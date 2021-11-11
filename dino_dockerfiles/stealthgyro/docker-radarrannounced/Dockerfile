FROM lsiobase/alpine.python:3.5
MAINTAINER sparklyballs

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

# add local files
COPY root/ /

# ports and volumes
EXPOSE 3467
WORKDIR /config
VOLUME /config /logs
