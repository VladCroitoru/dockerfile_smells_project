FROM node:8-alpine
MAINTAINER Richard Kojedzinszky <krichy@nmdps.net>

RUN apk --no-cache add -t .build-deps curl coreutils

RUN mkdir -p /opt/app && \
    curl -L https://github.com/zaidka/genieacs/archive/master.tar.gz | tar xzf - -C /opt/app --strip-components=1

WORKDIR /opt/app

RUN npm install && npm run configure && npm run compile

RUN apk --no-cache del .build-deps

EXPOSE 7777

ENV GENIEACS_MONGODB_CONNECTION_URL=mongodb://mongodb/genieacs \
    GENIEACS_REDIS_PORT=6379 \
    GENIEACS_REDIS_HOST=redis \
    GENIEACS_CWMP_INTERFACE=0.0.0.0 \
    GENIEACS_CWMP_PORT=7777 \
    GENIEACS_CWMP_SSL=false \
    GENIEACS_NBI_INTERFACE=0.0.0.0 \
    GENIEACS_NBI_PORT=7777 \
    GENIEACS_FS_INTERFACE=0.0.0.0 \
    GENIEACS_FS_PORT=7777 \
    GENIEACS_FS_IP=192.168.0.1 \
    GENIEACS_LOG_INFORMS=true \
    GENIEACS_DEBUG=false

# Cleanup
RUN rm -rf /root/.npm /tmp/npm-*

ADD assets /

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/bin/sh"]
