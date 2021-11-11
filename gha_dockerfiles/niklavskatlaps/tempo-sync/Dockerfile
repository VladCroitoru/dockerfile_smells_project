FROM node:16.8.0
ARG BUILD_CONTEXT

WORKDIR /usr/app
COPY package.json yarn.lock ./
COPY ./$BUILD_CONTEXT/package.json ./$BUILD_CONTEXT/
RUN yarn install --silent
COPY ./$BUILD_CONTEXT ./$BUILD_CONTEXT
