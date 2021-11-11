# create a container as "deploy" replacement
# it's a container to build the web app without changing the host
# "containerize all the things"

FROM tsari/wheezy-apache-php
MAINTAINER Tibor Sári <tiborsari@gmx.de>

# php
ENV DEBIAN_FRONTEND noninteractive
ENV NODE_VERSION 4.2.6
ENV NPM_VERSION 3.7.1
ENV COMPOSER_VERSION 1.4.1

RUN echo "deb http://ftp.de.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list.d/backports.list

RUN \
    apt-get update -qqy && \
    apt-get install --no-install-recommends -qqy --force-yes \
        autoconf \
        automake \
        bzip2 \
        ca-certificates \
        file \
        g++ \
        gcc \
        imagemagick \
        libbz2-dev \
        libc6-dev \
        libcurl4-openssl-dev \
        libevent-dev \
        libffi-dev \
        libgeoip-dev \
        libglib2.0-dev \
        libjpeg-dev \
        liblzma-dev \
        libmagickcore-dev \
        libmagickwand-dev \
        libmysqlclient-dev \
        libncurses-dev \
        libpng-dev \
        libpq-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libtool \
        libwebp-dev \
        libxml2-dev \
        libxslt-dev \
        libyaml-dev \
        make \
        patch \
        xz-utils \
        zlib1g-dev \
        openssh-client \
        mysql-client \
        rsync \
        subversion \
        sudo \
        unzip \
    && \
    apt-get -t wheezy-backports install -qqy --force-yes \
        git \
    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl --insecure -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl --insecure -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc


RUN npm install -g npm@$NPM_VERSION
RUN npm install -g node-gyp

# install composer
RUN curl -S --insecure -o /usr/local/bin/composer https://getcomposer.org/download/$COMPOSER_VERSION/composer.phar
RUN chmod +x /usr/local/bin/composer

# copy build script
COPY build.sh /usr/local/bin/build-application
RUN chmod +x /usr/local/bin/build-application

ADD https://raw.githubusercontent.com/tsari/docker-entrypoint/master/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Set up the command arguments
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD build-application