FROM node:4.8

MAINTAINER Kentaro Terada kterada.0509sg@gmail.com



RUN set -x \
    && echo deb http://ftp.jp.debian.org/debian/ jessie-backports main >> /etc/apt/sources.list \
    # System update
    && apt-get update \


    # Install npm (and its extra packages)
    && apt-get install -y  -t jessie-backports \
                openjdk-8-jre-headless \
                openjdk-8-jre \
                openjdk-8-jdk-headless \
                openjdk-8-jdk \
                ca-certificates-java \

    # Cleanup apt cache
    && apt-get clean && rm -r /var/lib/apt/lists/* \

    # Create app directory
    && mkdir -p /usr/src/app

WORKDIR /usr/src/app
ADD package.json .

RUN set -x \

    # Install npm packages
    && npm install \

    # Install gulp and grunt
    && npm install -g \
                gulp

CMD [ "npm" ]
