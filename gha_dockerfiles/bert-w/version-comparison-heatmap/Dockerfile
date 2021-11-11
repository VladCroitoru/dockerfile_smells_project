FROM node:15-slim AS node
FROM composer:latest AS composer
FROM php:7.4-fpm AS php

RUN apt-get update

RUN apt-get install -y curl git cloc

COPY --from=composer /usr/bin/composer /usr/local/bin/composer
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY --from=node /usr/local/bin/node /usr/local/bin/node
RUN ln -s /usr/local/lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm

WORKDIR /usr/app

COPY package*.json .
COPY composer*.json .
COPY ./src ./src
COPY ./import.js ./import.js
COPY ./main.js ./main.js

# Install app dependencies.
RUN npm install
RUN composer install

# Increase the amount of memory nodejs can allocate, this
# prevents JsInspect from running into the GC issues.
ENV NODE_OPTIONS=--max-old-space-size=4000

# Open a bash prompt, such that you can execute commands
# such as `cloc`.
ENTRYPOINT ["bash"]
