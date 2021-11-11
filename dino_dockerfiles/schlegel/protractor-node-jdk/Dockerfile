FROM openjdk:8-jdk

# environment variables
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 7.9.0

# replace shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# update the repository sources list
# and install dependencies
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y netcat \
    && apt-get install -y nginx \
    && apt-get -y autoclean

# Install nvm
# https://github.com/creationix/nvm#install-script
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash

# Install node and npm

RUN source $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default
# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -yqq update
RUN apt-get -yqq install google-chrome-stable

# Install Firefox
RUN curl http://mozilla.debian.net/archive.asc | apt-key add -
RUN echo "deb http://security.debian.org/ stretch/updates main" >> /etc/apt/sources.list.d/debian-mozilla.list
RUN apt-get -yqq update
RUN apt-get -yqq install firefox-esr

# Update to newest firefox
RUN mkdir /opt/firefox
RUN curl -o /opt/firefox/FirefoxSetup.tar.bz2 "https://download-installer.cdn.mozilla.net/pub/firefox/releases/55.0.1/linux-x86_64/en-US/firefox-55.0.1.tar.bz2"
RUN tar xjf /opt/firefox/FirefoxSetup.tar.bz2 -C /opt/firefox/
RUN mv /usr/lib/firefox-esr/firefox-esr /usr/lib/firefox-esr/firefox-esr_orig
RUN ln -s /opt/firefox/firefox/firefox /usr/lib/firefox-esr/firefox-esr

# Verify
RUN node -v
RUN npm -v
RUN google-chrome --version
RUN firefox --version
