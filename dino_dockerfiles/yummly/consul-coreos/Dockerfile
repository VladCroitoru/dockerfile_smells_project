FROM gliderlabs/consul-server:0.6
MAINTAINER Vadim Geshel, <vadim@yummly.com>

ENV GOMAXPROCS 10
ENV DOCKER_VERSION 1.8.3

RUN apk add --update bash

ADD https://get.docker.io/builds/Linux/x86_64/docker-${DOCKER_VERSION} /bin/docker
RUN chmod +x /bin/docker
RUN wget -O /tmp/ui.zip https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_web_ui.zip && \
    mkdir -p /ui && \
    cd /ui && \
    unzip -o /tmp/ui.zip && \
    rm /tmp/ui.zip

COPY ./etcd-bootstrap /bin/etcd-bootstrap
COPY ./start /bin/start
COPY ./agent /bin/agent

ENTRYPOINT ["/bin/start"]
CMD []
