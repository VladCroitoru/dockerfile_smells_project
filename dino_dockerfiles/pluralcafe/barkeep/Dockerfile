FROM node:alpine

LABEL maintainer="https://github.com/pluralcafe/barkeep" \
      description="Ambassador bot forked from mbilokonsky/ambassador"

ENV UID=992
ENV GID=992

WORKDIR /barkeep

RUN echo "@edge https://uk.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
 && apk -U upgrade \
 && apk add -t build-dependencies \
    build-base \
    postgresql-dev \
 && apk add tini \
            ca-certificates \
            tzdata \
 && update-ca-certificates \
 && rm -rf /tmp/* /var/cache/apk/* \
 && addgroup -g ${GID} barkeep \
 && adduser -h /barkeep -s /bin/sh -D -G barkeep -u ${UID} barkeep

COPY --chown=barkeep:barkeep package.json index.js /barkeep/

RUN yarn install

USER barkeep

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["yarn", "start"]
