FROM node:16.4.2-alpine as builder

# Get the necessary build tools
RUN apk upgrade -U -a \
  && apk add --no-cache \
  autoconf \
  automake \
  build-base \
  gcc \
  g++ \
  libtool \
  make \
  nasm \
  python \
  pkgconfig \
  && rm -rf /var/cache/* \
  && mkdir /var/cache/apk

# install dependencies
WORKDIR /app
COPY package*.json /app/
RUN npm install

# Get a clean image with pre-built node modules
FROM node:16.4.2-alpine
COPY --from=builder /app/node_modules /app/node_modules