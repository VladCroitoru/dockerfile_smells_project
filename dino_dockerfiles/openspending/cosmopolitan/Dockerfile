FROM gliderlabs/alpine:edge

MAINTAINER Paul Walsh <paulywalsh@gmail.com>

ENV LANG=en_US.UTF-8 \
    APP_DIR=/srv/app

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

RUN echo '@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/' >>  /etc/apk/repositories

RUN apk add --no-cache --virtual build-dependencies \
    build-base \
    linux-headers \
    python3-dev \
    libressl-dev \
    readline-dev \
    git \
    curl \
    postgresql-dev \
    libpng-dev \
    libjpeg-turbo-dev \
    libxml2-dev \
    libxslt-dev \
 && apk add --no-cache --update \
    python3 \
    readline \
    bzip2 \
    bash \
    gettext \
    ca-certificates \
    libressl \
    libpq \
    libjpeg-turbo \
    libpng \
    tzdata \
    py-psycopg2 \
    postgresql-client \
    make \
    geos@testing \
 && update-ca-certificates \
 && make install \
 && apk del build-dependencies

EXPOSE 5000

CMD make server

