FROM node:7.10.0-alpine
RUN apk add --update --virtual .build-dependencies git make gcc g++ python \
    && npm --ws:verbose install thomsch98/markserv -g \
    && apk del .build-dependencies
VOLUME ["/data"]
WORKDIR "/data"
CMD ["markserv", "-x", "-a", "0.0.0.0", "-p", "3080", "-l", "35729"]
USER 1000:1000