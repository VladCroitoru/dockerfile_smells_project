FROM node:boron
MAINTAINER Tatsuro Nakamura<me@tatsuroro.com>

# install hugo
RUN wget https://github.com/spf13/hugo/releases/download/v0.26/hugo_0.26_Linux-64bit.tar.gz \
    && tar -xzf hugo_0.26_Linux-64bit.tar.gz \
    && mv ./hugo /usr/local/bin

# install firebase
RUN npm install -g firebase-tools