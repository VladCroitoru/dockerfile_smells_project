FROM alpine:3.9
MAINTAINER Brint O'Hearn <brintly@gmail.com>

ENV DOCKER_COMPOSE_VERSION 1.24.0
ENV DOCKER_MACHINE_VERSION 0.16.0

RUN apk update && apk upgrade && apk add --no-cache bash curl python3 py3-yaml gcc python3-dev musl-dev libffi-dev openssl-dev make && \
  adduser -D -s /bin/bash user && \
  apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main --repository  http://dl-cdn.alpinelinux.org/alpine/edge/community docker && \
  curl -L https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-machine-`uname -s`-`uname -m` >/usr/local/bin/docker-machine && \
  chmod +x /usr/local/bin/docker-machine && \
  pip3 install -U pip && \
  pip3 install docker-compose==${DOCKER_COMPOSE_VERSION} && \
  apk del gcc python3-dev musl-dev libffi-dev openssl-dev make && \
  rm -rf `find / -regex '.*\.py[co]' -or -name apk`

WORKDIR /home/user
USER user
CMD ["/bin/bash"]
