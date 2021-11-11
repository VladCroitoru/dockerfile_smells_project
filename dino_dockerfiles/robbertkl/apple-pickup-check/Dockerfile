FROM node:alpine
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>

RUN apk add --no-cache \
        libc6-compat \
        openssl
RUN wget -qO /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
    chmod +x /usr/bin/dumb-init

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json ./
RUN yarn && yarn cache clean
COPY . .

ENV NODE_ENV=production
ENTRYPOINT [ "dumb-init", "node", "app" ]
CMD []
