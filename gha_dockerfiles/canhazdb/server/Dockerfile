FROM node:14-alpine

WORKDIR /app

RUN apk upgrade --update-cache --available && \
    apk add openssl && \
    rm -rf /var/cache/apk/*

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm ci
RUN npm install canhazdb-driver-ejdb

COPY . .

RUN ln -s /app/lib/cli.js /bin/canhazdb

ENTRYPOINT ["canhazdb"]

