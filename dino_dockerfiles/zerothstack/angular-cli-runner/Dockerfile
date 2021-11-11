FROM node:8.9.0

LABEL maintainer "Zak Henry <https://github.com/zerothstack>"


RUN curl 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y xvfb google-chrome-stable jq

ADD ./scripts/xvfb-launcher.sh /usr/local/bin/xvfb-launcher
