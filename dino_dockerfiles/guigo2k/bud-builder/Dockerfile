FROM docker:latest

ENV GLIBC_VERSION 2.23-r3
ENV DOCKER_COMPOSE_VERSION 1.11.2
ENV RANCHER_COMPOSE_VERSION v0.12.1

# defaults
RUN apk --update add git bash nodejs py-pip build-base ca-certificates

# glibc
ADD https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub
ADD https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk $PWD
RUN apk add glibc-${GLIBC_VERSION}.apk

# docker-compose
RUN pip install --upgrade pip && \
    pip install --upgrade docker-compose==${DOCKER_COMPOSE_VERSION} && \
    rm -rf `find / -regex '.*\.py[co]'`

# rancher-compose
ADD https://github.com/rancher/rancher-compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz /tmp
RUN cd /tmp && tar xvzf *.tar.gz && \
    mv ./*/rancher-compose /usr/local/bin && \
    chmod +x /usr/local/bin/* && rm -rf /tmp/*
