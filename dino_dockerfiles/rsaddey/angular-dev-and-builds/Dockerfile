# No thrills Ionic 2 and Angular 2 developer environment
# See https://blog.saddey.net/2016/07/03/using-docker-to-create-ionic-2-pwa-developer-environment
#
# docker run --name test -it \
#            -p 3000:3000 -p 3001:3001 -p 3003:3003 -p 5000:5000 \
#            -p 8100:8100 -p 8080:8080 -p 9876:9876 -p 35729:35729 \
#            -v /Users/rsaddey/Documents/PreApproval/Dockers/projects/:/projects \
#            rsaddey/angular-dev-and-builds
#
# rebuilt 28-oct-16 in order to use google-chrome-stable amd64 54.0.2840.71-1

FROM ubuntu:16.04

MAINTAINER Reiner Saddey <reiner@saddey.net>

LABEL Description="Proof of concept (work in progress) for developing and building Angular 2 applications"

# TODO reduce layers

RUN apt-get update

RUN apt-get install -y -q curl wget

# As of 03-jul-16: Ionic is not yet ready for Node.js 6, see https://github.com/driftyco/ionic-cli/issues/960
# RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -

# nodejs includes matching npm as well
# TODO add clean
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y -q \
    iputils-ping net-tools \
    nodejs \
    bzip2 \
    zip \
    libfontconfig \
    xvfb \
    google-chrome-stable \
    default-jre

# As of 03-jul-16: You have been warned, DO NOT push this button: RUN npm update -g npm
# https://github.com/npm/npm/issues/9863 Reinstalling npm v3 fails on Docker

# reqd when running as root TODO use some default user
RUN npm config set unsafe-perm true --global

# avoid global npms at all costs as they create flaky builds
## RUN npm install -g -y gulp@3.9.1
## RUN npm install -g -y ionic@beta

# TODO it'saterriblehack see https://github.com/paimpozhil/docker-novnc
RUN apt-get install -y -q \
    git x11vnc wget python python-numpy unzip && \
    cd /root && git clone https://github.com/kanaka/noVNC.git && \
    cd noVNC && ln -s vnc_auto.html index.html && \
    cd utils && git clone https://github.com/kanaka/websockify websockify && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



# Set the locale to German
RUN locale-gen de_DE.UTF-8
ENV LANG de_US.UTF-8
ENV LANGUAGE de_DE:de
ENV LC_ALL de_DE.UTF-8

COPY readme.txt /readme.txt
COPY start.sh /start.sh
RUN chmod +x /start.sh

# COPY xvfb.init /etc/init.d/xvfb
# RUN chmod +x /etc/init.d/xvfb && update-rc.d xvfb defaults

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# starts and stops xvfb on DISPLAY :99
ENTRYPOINT ["/entrypoint.sh"]

CMD '/start.sh';'bash'

# TODO check port list
# ports 8100 and 35729 used by ionic serve (default ports)
# 17-jul-16 expose port 5000 as well in order to run node.js (default port)
# 19-jul-16 expose ports 3000, 3001 and 3002 to support Angular using lite-server (default port = 3000)
# 25-jul-16 expose port 8080 for webpackServer prod
# 25-jul-16 expose port 9876 for Karma
# 28-jul-16 expose port 4444 for Selenium
# 28-jul-16 expose port 4000 for webpackServer dev ionic
# 01-aug-16 expose ports 5900 (vnc) 6080 (noVNC)
EXPOSE 3000 3001 3002 4000 4444 5000 5900 6080 8100 8080 9876 35729

# dbus said to fix some hangs running Chrome within Docker - who knows?
ENV DBUS_SESSION_BUS_ADDRESS="/dev/null" DISPLAY=:99

WORKDIR /projects

# Root for Angular and Ionic projects
# Do NOT use VOLUME statement as it may result in numerous orphaned volumes
# when innocent users or apps just run docker run --rm ... bash
# VOLUME /projects
