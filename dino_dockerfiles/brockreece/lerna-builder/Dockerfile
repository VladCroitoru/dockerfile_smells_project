FROM node:10-alpine

RUN apk add --no-cache bash git openssh zlib zlib-dev libpng libpng-dev libwebp libwebp-dev libjpeg-turbo libjpeg-turbo-dev nasm build-base automake autoconf file
RUN npm -g install lerna apollo@^2.0.0
RUN mkdir ~/.ssh
