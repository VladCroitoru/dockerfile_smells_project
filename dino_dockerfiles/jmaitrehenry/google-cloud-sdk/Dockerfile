FROM google/cloud-sdk:alpine
MAINTAINER Julien Maitrehenry <julien.maitrehenry@me.com>

RUN apk add --update --no-cache curl \
    && curl -fsSLO  https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz && tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin
