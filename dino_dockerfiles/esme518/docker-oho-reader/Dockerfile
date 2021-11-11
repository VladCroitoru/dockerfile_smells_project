#
# Dockerfile for oho-reader
#

FROM mhart/alpine-node as builder

RUN set -ex \
    && apk --update add --no-cache git \
    && git clone -b patch-1 --single-branch https://github.com/esme518/oho-reader.git \
    && cd oho-reader \
    && npm install \
    && npm audit fix \
    && npm run dist \
    && apk del git \
    && rm -rf /var/cache/apk

FROM mhart/alpine-node

COPY --from=builder /oho-reader/node_modules /oho-reader/node_modules
COPY --from=builder /oho-reader/dist /oho-reader/dist

WORKDIR /oho-reader/dist

EXPOSE 3001/tcp

CMD ["node", "app.js"]
