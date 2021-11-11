FROM alpine:3.5

ENV OPENLAYERS_VERSION=3.20.1

RUN apk update --no-cache \
    && apk add --no-cache \
        nodejs \
        openjdk8 \

    && mkdir -p /openlayers \
    && cd /openlayers \
    && npm install openlayers@$OPENLAYERS_VERSION \

    && chmod -R 0777 /openlayers

WORKDIR /build
VOLUME ["/build"]

ENTRYPOINT ["node", "/openlayers/node_modules/openlayers/tasks/build.js"]
CMD ["--help"]