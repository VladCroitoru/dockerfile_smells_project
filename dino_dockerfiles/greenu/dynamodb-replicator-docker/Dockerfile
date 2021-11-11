FROM node:9.10-alpine

RUN apk --no-cache update && \
    apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less git && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*

RUN npm install -g git+https://git@github.com/greenu/dyno.git
RUN npm install -g git+https://git@github.com/greenu/dynamodb-replicator.git

