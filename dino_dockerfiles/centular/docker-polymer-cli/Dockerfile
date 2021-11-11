###################################################################################
# Dockerfile to build a Polymer Dev Environment container images with Polymer-CLI
# Based on node:4-slim
#
# To build, do:
#   $ docker build -t centular/docker-polymer-cli .
#
###################################################################################

# Set the base image to node:4-slim
FROM buildpack-deps:jessie

#Based on image by Jeffery Bagirimvano <jeffery.rukundo@gmail.com>

MAINTAINER Wessel Pieterse <wessel@ordercloud.com>

ENV POLYMER_CLI_HOME /home/polymer
ENV user=polymer
ENV uid=1000
ENV group=polymer
ENV gid=1000

RUN groupadd --gid ${gid} ${user} \
  && useradd --uid ${uid} --gid ${group} --shell /bin/bash --create-home ${user}

ENV NPM_CONFIG_LOGLEVEL inf 
ENV NODE_VERSION 7.5.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz"  \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    npm install -g gulp bower polymer-cli generator-polymer-init-custom-build && \
    npm install git+https://github.com/centular-elements/generator-polymer-init-ct-app


EXPOSE 8080

RUN mkdir -p /home/${user}/app

USER ${user}

VOLUME /home/${user}/app

WORKDIR /home/${user}/app

CMD ["bash"]
