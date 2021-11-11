FROM alpine:latest
LABEL maintainer "DI GREGORIO Nicolas <nicolas.digregorio@gmail.com>"

### Environment variables
ENV LANG='en_US.UTF-8' \
    LANGUAGE='en_US.UTF-8' \
    TERM='xterm' 

### Install Application
RUN apk --no-cache upgrade && \
    apk add --no-cache --virtual=build-deps \
      unzip \
      gcc \
      make \
      python \
      curl && \
    apk add --no-cache --virtual=run-deps \
      ca-certificates \
      nodejs \
      nodejs-npm \
      su-exec && \
    curl -L https://github.com/TryGhost/Ghost/releases/download/0.11.11/Ghost-0.11.11.zip -o /tmp/ghost.zip && \
    mkdir /ghost && \
    unzip -uo /tmp/ghost.zip -d /ghost && \
    cd /ghost && \
    npm install --production && \
    npm install --save pg@latest && \
    npm cache clean && \
    apk del --no-cache --purge \
      build-deps  && \
    rm -rf /tmp/* \
           /var/cache/apk/*  \
           /var/tmp/*

### Volume
VOLUME ["/ghost/content"]

### Expose ports
EXPOSE 2368

### Running User: not used, managed by docker-entrypoint.sh
#USER ghost

### Start Mezzanine
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["ghost"]
