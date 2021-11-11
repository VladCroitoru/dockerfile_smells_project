# Base image for testing meteor applications using velocity-cli.
FROM ubuntu:14.04
MAINTAINER Lucid Programmer <lucidprogrammer@hotmail.com>
# -----language-pack-en----
# Refer to https://github.com/meteor/meteor/issues/4019
# -----libfreetype6 and fontconfig---------
# Avoid phantomjs errors like : error while loading shared libraries: libfreetype.so.6: cannot open shared object file: No such file or directory
RUN apt-get install -y curl wget git language-pack-en libfreetype6 fontconfig
RUN curl https://install.meteor.com | /bin/sh
# verify gpg and sha256: http://nodejs.org/dist/v0.10.30/SHASUMS256.txt.asc
# gpg: aka "Timothy J Fontaine (Work) <tj.fontaine@joyent.com>"
# gpg: aka "Julien Gilli <jgilli@fastmail.fm>"
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys 7937DFD2AB06298B2293C3187D33FF9D0246406D 114F43EE0176B71C7BC219DD50A3051F888C628D
ENV NODE_VERSION 0.10.40
ENV NPM_VERSION 2.14.1
RUN wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  	&& wget "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  	&& gpg --verify SHASUMS256.txt.asc \
  	&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  	&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  	&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \
  	&& npm install -g npm@"$NPM_VERSION" \
    && npm install velocity-cli -g \
  	&& npm cache clear
ENV VELOCITY_DEBUG 1
