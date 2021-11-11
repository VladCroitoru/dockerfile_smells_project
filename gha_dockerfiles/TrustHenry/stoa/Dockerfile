# From Agora Runner
FROM node:14.15.4-alpine3.12
RUN apk add --no-cache git py-pip alpine-sdk \
    bash autoconf libtool automake

WORKDIR /stoa/wd/

ADD . /stoa/bin/
RUN npm ci --prefix /stoa/bin/

# Starts a node process, which compiles TS and watches `src` for changes
ENTRYPOINT [ "/stoa/bin/docker/entrypoint.sh" ]
