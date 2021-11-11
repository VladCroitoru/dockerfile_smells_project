FROM alpine:edge
MAINTAINER Porawit Poboonma <ball6847@gmail.com>

ADD ./ /app

ENV TERM=xterm-256color
ENV COMPOSE_PROJECT_NAME=webstack
ENV DOCKER_API_VERSION=1.22
WORKDIR /app/core/webstack

RUN apk add --update --no-cache gcc musl-dev python-dev py-pip bash wget ca-certificates openssl docker && \
    sh -c "wget https://bootstrap.pypa.io/ez_setup.py -O - | python" && \
    pip install -r requirements.txt && \
    pip install docker-compose && \
    apk del gcc musl-dev python-dev

VOLUME [ "/var/lib/webstack/data", "/data/www", "/data/logs", "/data/vhosts" ]

EXPOSE 8000

ENTRYPOINT sh -c "/app/core/webstack/entrypoint.sh"
