FROM ubuntu:latest
MAINTAINER Mengyang Li <mayli.he@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update && apt-get install -y curl python-minimal build-essential
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get install -y nodejs
RUN cd && npm install tty.js
ADD _tty_js /root/.tty.js/config.js
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8080
WORKDIR /root
ENTRYPOINT ["/root/node_modules/tty.js/bin/tty.js"]
