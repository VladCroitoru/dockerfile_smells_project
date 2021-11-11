FROM node:latest

RUN \
# update packages index
    apt-get update \
# install packages in noninteractive mode
    && DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
        chromium \
        libgconf-2-4 \
        openjdk-7-jre-headless \
# remove cached packages list
# to reduce image size
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN /usr/bin/chromium
