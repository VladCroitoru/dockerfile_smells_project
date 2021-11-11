FROM node:alpine
MAINTAINER butlerx@notthe.cloud
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN apk add --no-cache git build-base file nasm autoconf libpng-dev openssl && yarn
VOLUME /usr/src/app/pluginCode/bookclub/config /usr/src/app/pluginCode/countdown/config
CMD yarn start
