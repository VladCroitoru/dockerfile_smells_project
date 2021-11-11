FROM node:latest

MAINTAINER Florian Wittmann <dev@florianwittmann.de>

RUN yarn global add firebase-tools
RUN yarn global add netlify-cli

RUN apt-get update
RUN apt-get -y install default-jre xvfb chromium libappindicator1 fonts-liberation

ADD xvfb-chromium /usr/bin/xvfb-chromium

RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser 
RUN chmod +777 /usr/bin/google-chrome
RUN chmod +777 /usr/bin/xvfb-chromium
RUN chmod +777 /usr/bin/chromium-browser

WORKDIR /workspace
