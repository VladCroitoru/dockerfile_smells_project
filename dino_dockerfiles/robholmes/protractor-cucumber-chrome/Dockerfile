FROM node:slim

MAINTAINER i6 Dev Team <dev-team@i6.io>

WORKDIR /tmp

RUN npm install -g protractor@3.1.1 cucumber@0.9.1 chai chai-as-promised protractor-cucumber-framework cucumber-junit dateformat request && \
    webdriver-manager update && \
    apt-get update && \
    apt-get install -y xvfb wget curl openjdk-7-jre gconf-service libgconf-2-4 libnspr4 libnss3 libpango1.0-0 libappindicator1 libcurl3 libxss1 fonts-liberation xdg-utils && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    curl -L -o google-chrome.deb https://s3.amazonaws.com/circle-downloads/google-chrome-stable_current_amd64_47.0.2526.73-1.deb && \
    dpkg -i google-chrome.deb && \
    sed -i 's|HERE/chrome\"|HERE/chrome\" --disable-setuid-sandbox|g' /opt/google/chrome/google-chrome && \
    apt-get clean && \
    rm google-chrome.deb && \
    mkdir /protractor && \
    cd /protractor

WORKDIR /protractor

ENV NODE_PATH /usr/local/lib/node_modules
