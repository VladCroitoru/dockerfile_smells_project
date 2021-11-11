FROM node:16.9.1-alpine3.14

WORKDIR /lint
COPY package.json package-lock.json .remarkrc.yaml ./
RUN npm install \
    && npm link remark-cli \
    && apk add --no-cache git~=2.32

WORKDIR /lint/input
ENTRYPOINT ["/usr/local/bin/remark"]
