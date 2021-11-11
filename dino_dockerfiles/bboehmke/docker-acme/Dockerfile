FROM python:3.6-alpine

MAINTAINER Benjamin Böhmke <benjamin@boehmke.net>

ENV DOCKER_GEN_VERSION=0.7.3 \
    DOCKER_CLIENT_VERSION=17.09.0

RUN apk add --no-cache openssl wget supervisor && \
    wget https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_CLIENT_VERSION}-ce.tgz && \
    tar xvzf docker-${DOCKER_CLIENT_VERSION}-ce.tgz docker/docker && mv docker/docker /bin/docker && \
    rm -r docker-${DOCKER_CLIENT_VERSION}-ce.tgz docker && \
    wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    tar -C /bin/ -xvzf docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    rm -r docker-gen-alpine-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    mkdir /acme/

ADD https://raw.githubusercontent.com/diafygi/acme-tiny/master/acme_tiny.py /acme_tiny.py
ADD app.py /app.py
ADD crt_domains.ini.tmpl /crt_domains.ini.tmpl
COPY supervisor/ /etc/supervisor.d/

VOLUME /acme/config/
VOLUME /acme/crt/
VOLUME /acme/acme_challenge/

ENTRYPOINT ["/usr/bin/supervisord", "-n"]
