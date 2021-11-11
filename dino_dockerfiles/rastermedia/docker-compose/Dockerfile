FROM tatsushid/tinycore-python:2.7

MAINTAINER Adam Segal <adam@rastermedia.com>

ENV DOCKER_COMPOSE_VERSION 1.3.0

RUN pip install -U docker-compose==${DOCKER_COMPOSE_VERSION}

# This container is a chrooted docker-compose
WORKDIR /app
ENTRYPOINT ["/usr/local/bin/docker-compose"]
CMD ["--version"]
