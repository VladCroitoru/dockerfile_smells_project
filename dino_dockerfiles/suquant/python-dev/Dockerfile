FROM alpine:3.5
MAINTAINER George Kutsurua <g.kutsurua@gmail.com>

RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories &&\
    apk add --no-cache sudo bash curl make perl rsync openssl openssh-client nginx \
                       libpq libffi libffi-dev libxml2 libxml2-dev libbz2 \
                       libxslt libxslt-dev libtool libstdc++ zlib zlib-dev git unzip \
                       libjpeg libjpeg-turbo libjpeg-turbo-dev openjpeg openjpeg-dev \
                       libpng libpng-dev tiff tiff-dev freetype freetype-dev lcms2 lcms2-dev \
                       libwebp libwebp-dev tcl tcl-dev imagemagick imagemagick-dev imagemagick-c++ \
                       json-c json-c-dev jsoncpp jsoncpp-dev python3 python3-dev musl musl-dev \
                       postgis-dev@testing postgis@testing linux-headers gcc g++ coreutils ca-certificates \
                       pcre-dev pcre libpcre32 &&\
    wget -O - https://bootstrap.pypa.io/get-pip.py | python3

ENV LANG=en_US.utf8 \
    LC_ALL=en_US.utf8 \
    LANGUAGE=en_US.utf8 \
    KUBECTL_VERSION=v1.6.6 \
    DOCKER_VERSION=1.13.1 \
    REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

RUN curl -o docker-$DOCKER_VERSION.tgz https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz && \
    tar -xzf docker-$DOCKER_VERSION.tgz -C /usr/bin --strip-components=1 && \
    rm -rf docker-$DOCKER_VERSION.tgz && \
    curl -o /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl && \
    chmod +x /usr/bin/kubectl

COPY requirements.txt /requirements.txt
COPY gitlab-runner-helper /usr/bin/gitlab-runner-helper

RUN pip install --upgrade -r /requirements.txt
