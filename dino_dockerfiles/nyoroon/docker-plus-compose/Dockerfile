ARG DOCKER_VERSION=18.03.1
FROM docker:${DOCKER_VERSION}

ARG COMPOSE_VERSION=1.21.2

RUN apk add --no-cache python3
RUN pip3 install --no-cache-dir docker-compose==${COMPOSE_VERSION}
