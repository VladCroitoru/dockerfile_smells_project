FROM node:16.7.0-alpine3.14 AS builder
WORKDIR /app
COPY package.json ./
RUN apk add --no-cache git
RUN yarn install --production
COPY . .
RUN node --max_old_space_size=512 node_modules/.bin/react-scripts build

FROM php:7.2-apache
RUN pecl install redis && docker-php-ext-enable redis
WORKDIR /var/www/html/
COPY --from=builder /app/build .

