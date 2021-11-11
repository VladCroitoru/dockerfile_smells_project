FROM ubuntu:latest
LABEL maintainer "infiniteproject@gmail.com"

ENV DOCKER_HOST unix:///tmp/docker.sock
ENV DOCKER_GEN_VERSION 0.7.3
ENV DEBIAN_FRONTEND noninteractive

VOLUME /var/lib/tor
WORKDIR /app

RUN apt-get update && \
    apt-get -y --no-install-recommends install \
        tor \
        wget \
        ca-certificates \
        supervisor

RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz && \
    rm docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz
	
RUN apt-get clean && \
    rm -fr /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*

COPY torrc.tmpl /app/torrc.tmpl
COPY supervisord.conf /app/supervisord.conf
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["supervisord", "-c", "/app/supervisord.conf"]
