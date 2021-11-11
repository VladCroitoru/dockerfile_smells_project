FROM mvertes/alpine-mongo:3.6.1-0

LABEL maintainer="warhorse@thedarkcloud.net"

ARG BUILD_RFC3339="1970-01-01T00:00:00Z"
ARG COMMIT="local"
ARG VERSION="v1.0.1"

EXPOSE 11015

RUN apk add --update libressl
RUN apk add go curl bash libc6-compat git musl-dev && rm -fr /var/cache/apk/*; exit 0

ENV LAIRDB_HOST=lairdb
ENV MONGO_URL=mongodb://$LAIRDB_HOST:27017/lair
ENV API_LISTENER=0.0.0.0:11015
ENV TRANSFORM_DIR=/tmp
ENV GOPATH=$HOME/go
ENV PATH=$PATH:$GOPATH/bin

RUN go get -v github.com/x-a-n-d-e-r-k/api-server

CMD mkdir /plugins
CMD mkdir /scripts
COPY ./db_init.js /scripts/
COPY ./docker-entrypoint.sh /scripts/
COPY ./wait.sh /scripts/
CMD chmod +x /scripts/docker-entrypoint.sh 
RUN chmod +x /scripts/wait.sh

ENTRYPOINT ["/scripts/docker-entrypoint.sh"]

LABEL org.opencontainers.image.ref.name="warhorse/lair-api" \
      org.opencontainers.image.created=$BUILD_RFC3339 \
      org.opencontainers.image.authors="warhorse <warhorse@thedarkcloud.net>" \
      org.opencontainers.image.documentation="https://github.com/war-horse/docker-lair-api/README.md" \
      org.opencontainers.image.description="lair-api Docker Build" \
      org.opencontainers.image.licenses="GPLv3" \
      org.opencontainers.image.source="https://github.com/war-horse/docker-lair-api" \
      org.opencontainers.image.revision=$COMMIT \
      org.opencontainers.image.version=$VERSION \
      org.opencontainers.image.url="https://hub.docker.com/r/warhorse/lair-api/"

ENV BUILD_RFC3339 "$BUILD_RFC3339"
ENV COMMIT "$COMMIT"
ENV VERSION "$VERSION"