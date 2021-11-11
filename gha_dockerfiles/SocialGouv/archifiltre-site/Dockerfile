FROM node:14-alpine as builder

COPY . .

RUN apk add automake autoconf libtool dpkg pkgconfig nasm libpng libpng-dev g++ make

RUN yarn --frozen-lockfile --prefer-offline && yarn cache clean
RUN yarn build

FROM ghcr.io/socialgouv/docker/nginx:6.53.2

COPY --from=builder ./public /usr/share/nginx/html
