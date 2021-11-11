FROM node:14.17.6-buster-slim

USER root
RUN apt-get update && apt-get install -y git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g @remix-project/remixd

RUN sed -i s/127.0.0.1/0.0.0.0/g /usr/local/lib/node_modules/\@remix-project/remixd/websocket.js

COPY origins.json /usr/local/lib/node_modules/\@remix-project/remixd/

EXPOSE 65520
EXPOSE 8080 

ENTRYPOINT ["/usr/local/bin/remixd", "-s", "/app"]