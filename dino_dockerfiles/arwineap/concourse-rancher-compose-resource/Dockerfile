FROM node:6
COPY package.json /opt/resource/package.json
RUN cd /opt/resource && \
  npm install && \
  npm cache clear
COPY check.js /opt/resource/check
COPY in.js /opt/resource/in
COPY out.js /opt/resource/out
RUN chmod +x /opt/resource/*
ENV RANCHER_COMPOSE_VERSION v0.12.5
ADD https://github.com/rancher/rancher-compose/releases/download/$RANCHER_COMPOSE_VERSION/rancher-compose-linux-amd64-$RANCHER_COMPOSE_VERSION.tar.gz /tmp/rancher-compose.tar.gz
RUN cd /tmp && \
  tar xfz rancher-compose.tar.gz && \
  cp rancher-compose-$RANCHER_COMPOSE_VERSION/rancher-compose /usr/local/bin
