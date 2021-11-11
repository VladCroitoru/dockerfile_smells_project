FROM centos:7

MAINTAINER tobilg@gmail.com

ENV KONG_VERSION 0.8.3
ENV DOCKERIZE_VERSION v0.2.0

RUN yum install -y https://github.com/Mashape/kong/releases/download/$KONG_VERSION/kong-$KONG_VERSION.el7.noarch.rpm wget && \
    yum clean all && \
    wget -nv https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz && \
    tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY config/kong.yml.template /etc/kong/

COPY docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
