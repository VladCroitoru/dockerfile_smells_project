FROM  ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive 
ENV DEBCONF_NONINTERACTIVE_SEEN true

#################################################################
# Install java
#################################################################

RUN apt-get update && \
    apt-get install -y software-properties-common  \
    git \
    curl \
    wget \
    zip \
    unzip \
    tzdata && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

RUN  cp /usr/share/zoneinfo/Europe/Copenhagen /etc/localtime \
    && echo "Europe/Copenhagen" > /etc/timezone

ENV TZ Europe/Copenhagen

#################################################################
# Install maven
#################################################################

ARG MAVEN_VERSION=3.5.4
ARG USER_HOME_DIR="/root"
ARG BASE_URL=https://www-eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/
ARG SHA=22cac91b3557586bb1eba326f2f7727543ff15e3

RUN curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz 
RUN echo "${SHA}  /tmp/apache-maven.tar.gz" | sha1sum -c - 
## Verified, let's install 
RUN mkdir -p /usr/share/maven /usr/share/maven/ref 
RUN tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 
RUN rm -f /tmp/apache-maven.tar.gz 
RUN ln -s /usr/share/maven/bin/mvn /usr/bin/mvn 

#################################################################
# Install Nodejs
#################################################################
RUN  apt-get update \
  && apt-get install -y git \
  libpq-dev \
  apt-transport-https \
  make \
  python-pip \
  python2.7 \
  python2.7-dev \
  ssh \  
  xz-utils  \
  && rm -rf /var/lib/apt/lists/*

RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

# gpg keys listed at https://github.com/nodejs/node#release-team
RUN set -ex \
  && for key in \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    56730D5401028683275BD23C23EFEFE93C4CFFFE \
    77984A986EBC2AA786BC0F66B01FBB92821C587A \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done

ENV NODE_VERSION 8.11.2

RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    ppc64el) ARCH='ppc64le';; \
    s390x) ARCH='s390x';; \
    arm64) ARCH='arm64';; \
    armhf) ARCH='armv7l';; \
    i386) ARCH='x86';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -SLO --compressed "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs
  
RUN npm install npm@6.4.0 -g  
RUN npm install --unsafe-perm -g @angular/cli findup-sync typescript


##################################################
# Headless chrome 
##################################################

RUN  apt-get update \
  && apt-get install -y build-essential \
  ca-certificates \
  gcc \
  apt-transport-https \
  && rm -rf /var/lib/apt/lists/*

# Install deps + add Chrome Stable + purge all the things
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/chrome.list 
RUN apt-get update -qqy 
RUN apt-get -qqy install  google-chrome-stable 
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*
