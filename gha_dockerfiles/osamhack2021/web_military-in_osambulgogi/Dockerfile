FROM node:16-alpine3.14

COPY . /app

RUN apk add --no-cache nginx openssl postgresql-client \
    && yarn --cwd /app/WEB\(BE\) install \
    && yarn --cwd /app/WEB\(BE\) build \
    && yarn --cwd /app/WEB\(FE\) install \
    && yarn --cwd /app/WEB\(FE\) build \
    && yarn global add pm2

ENTRYPOINT /app/entrypoint.sh
