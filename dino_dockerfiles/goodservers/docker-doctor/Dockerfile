FROM mhart/alpine-node:10.16.0 AS builder
LABEL maintainer="Tom Wagner <tomas.wagner@gmail.com>"

# create workdir
RUN mkdir -p /app

# set workdir
WORKDIR /app

# cache web and common dir dependencies
COPY yarn.lock package.json ./
RUN yarn install

# copy app code
COPY . .

ENV NODE_ENV=production
RUN yarn build
RUN yarn pkg


# And then copy pkg binary from that stage to the smaller base image
FROM alpine:3.10
RUN apk update && \
  apk add --no-cache libstdc++ libgcc ca-certificates && \
  rm -rf /var/cache/apk/*
WORKDIR /app

COPY --from=builder /app/pkg .
ENV NODE_ENV=production

ENTRYPOINT ./docker-doctor