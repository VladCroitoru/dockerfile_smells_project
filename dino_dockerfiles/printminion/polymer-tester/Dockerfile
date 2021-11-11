FROM node:latest
MAINTAINER Misha M.-Kupriyanov <m.kupriyanov@gmail.com>

ENV DISPLAY=:0
ENV RESOLUTION=1366x768

WORKDIR /root

RUN set -xe \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update -yqqq \
    && apt-get install -qq -y google-chrome-stable

#try to fool google-chrome to run without sandbox
RUN mv /usr/bin/google-chrome /usr/bin/google-chrome-orig \
    && echo '#!/bin/bash' > /usr/bin/google-chrome \
    && echo '/usr/bin/google-chrome-orig --no-sandbox --disable-setuid-sandbox --allow-sandbox-debugging "$@"' >> /usr/bin/google-chrome  \
    && chmod +x /usr/bin/google-chrome

RUN apt-get install -qq -y xvfb

#install firefox
RUN apt-get install -qq -y pkg-mozilla-archive-keyring \
    && echo "deb http://mozilla.debian.net/ jessie-backports firefox-release" >>  /etc/apt/sources.list \
    && apt-get update -qq \
    && apt-get install -qq -y pkg-mozilla-archive-keyring firefox


#install Java 8
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list \
    && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 \
    && apt-get -qq update \
    && echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
    && apt-get install -y -qq oracle-java8-installer \
    && apt-get install -y -qq oracle-java8-set-default

RUN npm install -g bower \
    && echo '{ "allow_root": true, "gitUseHttps": true }' > ~/.bowerrc \
    && echo "N\n" | bower

RUN npm install -g polymer-cli
ADD startup.sh /

RUN chmod +x /startup.sh
    
ENTRYPOINT ["/startup.sh"]

#to run tests use
#Xvfb :0 -ac +extension RANDR -screen 0 1366x768x24 &
#xvfb-run polymer test -l firefox
#xvfb-run polymer test -l chrome
