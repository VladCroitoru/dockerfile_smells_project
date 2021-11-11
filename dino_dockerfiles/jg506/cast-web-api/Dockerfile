FROM node:alpine
WORKDIR /cast-web-api
RUN apk add --update git && \
  rm -rf /tmp/* /var/cache/apk/*
RUN git clone https://github.com/vervallsweg/cast-web-api.git . && \
  npm install

