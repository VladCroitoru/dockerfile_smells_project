FROM node:14.18.0-stretch

USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/ssl/certs/* && \
    mkdir -p /additional_certs

RUN npm install -g @remix-project/remixd

RUN sed -i s/127.0.0.1/0.0.0.0/g /usr/local/lib/node_modules/\@remix-project/remixd/websocket.js

COPY origins.json /usr/local/lib/node_modules/\@remix-project/remixd/

EXPOSE 65520, 8080

ENTRYPOINT ["/usr/local/bin/remixd", "-s", "/app"] 