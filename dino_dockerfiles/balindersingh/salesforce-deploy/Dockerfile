FROM mcr.microsoft.com/dotnet/core/sdk:2.2-alpine AS build
MAINTAINER Balinder Singh <bsbhinder@outlook.com>
RUN apk update
RUN apk add bash
RUN apk add openjdk8
RUN apk add jq
RUN apk add --update nodejs npm
RUN npm install -g grunt-cli
RUN npm install -g sfdx-cli
RUN echo "DOTNET version:"
RUN dotnet --version
RUN apk add chromium
RUN apk add chromium-chromedriver
RUN apk add apache-ant --update-cache \
	--repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \
	--allow-untrusted
RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

# adding one more alpine repo (the testing) one in the reference repos so that we can add original firefox browser .
# On main/community repos we don't have firefox browser but Firefox ESR which didn't work with our solution
RUN \
echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories && \
echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update && apk upgrade && \
apk add firefox tar unzip xvfb && \
rm -rf /var/cache/apk/*

RUN \
# Create firefox + xvfb runner (it is in-memory display server to run firefox in headless mode)
mv /usr/bin/firefox /usr/bin/firefox-origin && \
echo $'#!/usr/bin/env sh\n\
Xvfb :0 -screen 0 1920x1080x24 -ac +extension GLX +render -noreset & \n\
DISPLAY=:0.0 firefox-origin $@ \n\
killall Xvfb' > /usr/bin/firefox && \
chmod +x /usr/bin/firefox

# geckodriver (it is the driver for firefox)
RUN curl https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz -O -L && ls && \
	tar -zxvf geckodriver-v0.24.0-linux64.tar.gz && \
	mv ./geckodriver /usr/local/bin/ && \
	chmod a+x /usr/local/bin/geckodriver

ENTRYPOINT ["/bin/bash"]

ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin