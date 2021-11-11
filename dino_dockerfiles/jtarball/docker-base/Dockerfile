#
# A base image for django backend web application 
#
# Please README.md for how to use this Docker Container
#
# This code is inspired from the source code:
# https://github.com/smaato/docker-quickstart
# https://www.smaato.com/quickstart-a-web-development-stack-using-vagrant-docker/ 
# 
# Also tried to keep to best practice: https://github.com/docker-library/official-images
# 
# Remember to set the following environment variables:
# ENV_TYPE

FROM debian:8.2
MAINTAINER James Tarball <james.tarball@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV APP_DIR /app
ENV BUILD_DIR /tmp
#ENV ENV_TYPE prod
# Node
ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 5.0.0

# Add Label Badges to Dockerfile powered by microbadger
ARG VCS_REF

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="e.g. https://github.com/microscaling/microscaling"


# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r app --gid=999 && useradd -r -g app --uid=999 app

# Basic stuff...
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN apt-get -yq update && apt-get -yq install \
        git \
        curl \
        net-tools \
        sudo \
        bzip2 \
        libpng-dev \
        locales-all \
        build-essential \
        postgresql-contrib \
        npm \
        vim \
        bash-completion \
        python-dev \
        python \
        python-pip \
        postgresql \
        python-psycopg2 \
        openssh-server \
        openssh-sftp-server \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*


# gpg keys listed at https://github.com/nodejs/node
RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --verify SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc

# Node, Yeoman and a few more useful stuff
RUN npm install -g yo && \
    npm install -g webpack && \
    npm install -g babel-cli && \
    npm install -g bower

# grab gosu for easy step-down from root
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
    && wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture)" \
    && wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-architecture).asc" \
    && gpg --verify /usr/local/bin/gosu.asc \
    && rm /usr/local/bin/gosu.asc \
    && chmod +x /usr/local/bin/gosu

# shellshock fix
RUN apt-get -yq update && apt-get -yq install  --only-upgrade bash \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Set the timezone.
RUN sudo echo "Europe/London" > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata

# Add a yeoman user because grunt etc. doesn't like being root
# Yeoman user is required if this is used as part of a yeoman generator
RUN adduser --disabled-password --gecos "" yeoman && \
  echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# set HOME so 'npm install' and 'bower install' don't write to /
ENV HOME /home/yeoman
ENV LANG en_GB.UTF-8

RUN mkdir -p $APP_DIR
RUN mkdir -p $BUILD_DIR
WORKDIR $APP_DIR

RUN chown yeoman:yeoman $APP_DIR
RUN chown yeoman:yeoman $BUILD_DIR

# Always run as the yeoman user - YO commands will not work otherwises!
USER yeoman

#VOLUME $APP_DIR

CMD /bin/bash
