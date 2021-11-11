FROM alpine:edge

ENV DOCKER_MACHINE_NAME=default
ENV DOCKER_MACHINE_PORT=2376

RUN apk -q update && apk add bash docker curl openssh-client py2-pip

RUN pip install docker-compose
RUN docker-compose --version

RUN curl -L https://github.com/docker/machine/releases/download/v0.8.2/docker-machine-`uname -s`-`uname -m` > /usr/bin/docker-machine && chmod +x /usr/bin/docker-machine
RUN docker-machine --version

RUN pip install awscli

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
