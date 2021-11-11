FROM node:0

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

COPY entrypoint.js /opt/autobump/entrypoint.js

WORKDIR /opt/autobump

RUN /usr/local/bin/npm install github

ENTRYPOINT ["/usr/local/bin/node", "/opt/autobump/entrypoint.js"]
