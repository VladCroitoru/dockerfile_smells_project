FROM alpine:latest
MAINTAINER Alexis Horgix Chotard <alexis.horgix.chotard@gmail.com>

ENV TARBALL https://github.com/saltstack/salt/archive/develop.tar.gz
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk --update --update-cache upgrade \
    && apk add \
        py-pip \
        python-dev \
        ca-certificates \
        swig \
        openssl \
        gcc \
        g++ \
        libc-dev \
    && update-ca-certificates \
    && pip install --upgrade pip
RUN wget ${TARBALL} \
    && tar xzf develop.tar.gz \
    && pip install ./salt-develop/

# 4505 = Salt Pub ; 4506 = Salt Req
EXPOSE 4505 4506

CMD /usr/bin/salt-master
