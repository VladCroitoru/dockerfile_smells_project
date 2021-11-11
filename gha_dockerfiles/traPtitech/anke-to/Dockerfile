# syntax = docker/dockerfile:1.3.0

# build backend
FROM golang:1.17.3-alpine as server-build
RUN --mount=type=cache,target=/var/cache/apk \
  apk add --update git

WORKDIR /github.com/traPtitech/anke-to

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN --mount=type=cache,target=/root/.cache/go-build \
  go build -o /anke-to -ldflags "-s -w"

#build frontend
FROM node:16.13.0-alpine3.14 as client-build
WORKDIR /github.com/traPtitech/anke-to/client
RUN --mount=type=cache,target=/var/cache/apk \
  apk add --update --no-cache python3 make g++
COPY client/package.json client/package-lock.json ./
RUN --mount=type=cache,target=/root/.npm \
  npm ci
COPY client .
RUN --mount=type=cache,target=/github.com/traPtitech/anke-to/client/node_modules/.cache \
  npm run build


# run
FROM alpine:3.14.2
WORKDIR /app

RUN apk --update --no-cache add tzdata \
  && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && apk del tzdata \
  && mkdir -p /usr/share/zoneinfo/Asia \
  && ln -s /etc/localtime /usr/share/zoneinfo/Asia/Tokyo
RUN apk --update --no-cache add ca-certificates \
  && update-ca-certificates \
  && rm -rf /usr/share/ca-certificates

COPY --from=server-build /anke-to ./
COPY --from=client-build /github.com/traPtitech/anke-to/client/dist ./client/dist/
ENTRYPOINT ./anke-to
