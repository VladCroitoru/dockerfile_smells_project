FROM alpine

MAINTAINER Virgil Chereches <virgil.chereches@gmx.net>

RUN apk add --update bash && apk add curl && \
    apk add git && rm -rf /var/cache/apk/*

RUN cd /tmp && \
    curl -Lk https://releases.rancher.com/compose/v0.8.6/rancher-compose-linux-amd64-v0.8.6.tar.gz > rancher-compose.tar.gz && \
    tar xzvf rancher-compose.tar.gz && \
    mv rancher-compose*/rancher-compose /usr/local/bin && \
    rm -rf rancher-compose.tar.gz && rmdir rancher-compose*

RUN sed -i -e 's/ash/bash/g' /etc/passwd

COPY rancher_compose_env /root/.bashrc

CMD /bin/bash
