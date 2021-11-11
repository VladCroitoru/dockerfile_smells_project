# No thrills Ionic 2 and Angular 2 developer environment
# See https://blog.saddey.net/2016/07/03/using-docker-to-create-ionic-2-pwa-developer-environment
# and https://angular.io/docs/ts/latest/quickstart.html
# and http://ionicframework.com/docs/v2/getting-started/tutorial/
#
# docker run --name jump-ionic2 -it \
#            -p 3000:3000 -p 5000:5000 -p 8100:8100 \
#            -p 8080:8080 -p 9876:9876 -p 35729:35729 \
#            -v /Users/rsaddey/Documents/PreApproval/Dockers/projects/:/projects \
#            rsaddey/jump-ionic2
#

FROM ubuntu:16.04

MAINTAINER Reiner Saddey <reiner@saddey.net>

LABEL Description="Interactive Ionic 2 Framework example using volume /projects as the root for your app directories"

# 26-jul-16: add wget used by recipes for installing Chrome
RUN apt-get update && apt-get install -y -q curl wget

# As of 03-jul-16: Ionic is not yet ready for Node.js 6, see https://github.com/driftyco/ionic-cli/issues/960
# RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -

# nodejs includes matching npm as well
# 25-jul-16: bzip2 and libfontconfig needed by npm install phantomjs (e.g. for Karma testing)
# 26-jul-16: xvfb chrome-browser
# 28-jul-16: default-jre (selenium / protractor)
# 28-jul-16 prb solving: iputils-ping net-tools (netstat)
# 28-jul-16 Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y -q \
    iputils-ping net-tools \
    nodejs \
    bzip2 \
    libfontconfig \
    xvfb \
    google-chrome-stable \
    default-jre \
    && apt-get -y autoclean \
    && rm -rf /var/lib/apt/lists/*

# As of 03-jul-16: You have been warned, DO NOT push this button: RUN npm update -g npm
# https://github.com/npm/npm/issues/9863 Reinstalling npm v3 fails on Docker

# reqd when running as root, i.e. auto-always --unsafe-perm cli option
RUN npm config set unsafe-perm true --global

# Install Ionic 2
RUN npm install -g -y \
               ionic@beta

COPY readme.txt /readme.txt
COPY start.sh /start.sh

WORKDIR /projects

CMD bash -C '/start.sh';'bash'

# ports 8100 and 35729 used by ionic serve (default ports)
# 17-jul-16 expose port 5000 as well in order to run node.js (default port)
# 19-jul-16 expose ports 3000, 3001 and 3002 to support Angular using lite-server (default port = 3000)
# 25-jul-16 expose port 8080 for webpackServer prod
# 25-jul-16 expose port 9876 for Karma
EXPOSE 3000 5000 8100 8080 9876 35729

# Root for Angular and Ionic projects
# Do NOT use VOLUME statement as it may result in numerous orphaned volumes
# when innocent users or apps just run docker run --rm ... bash
# VOLUME /projects
