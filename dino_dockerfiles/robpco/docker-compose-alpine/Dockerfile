FROM alpine:latest

LABEL maintainer Robert Peteuil <https://github.com/robertpeteuil>

ENV DOCKER_COMPOSE_VERSION 1.24.0

RUN apk --update add py-pip
RUN apk --update add --virtual build-dependencies gcc python2-dev libffi-dev openssl-dev musl-dev make &&\
    pip install -U docker-compose==${DOCKER_COMPOSE_VERSION} &&\
    apk del build-dependencies &&\
    rm -rf `find / -regex '.*\.py[co]' -or -name apk`

WORKDIR /app
ENTRYPOINT ["/usr/bin/docker-compose"]
CMD ["--version"]
