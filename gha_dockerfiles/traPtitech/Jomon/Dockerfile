## build backend
FROM golang:1.13.5-alpine as server-build

WORKDIR /github.com/traPtitech/Jomon
COPY go.mod go.sum ./
RUN go mod download

COPY ./storage ./storage
COPY ./main.go ./
COPY ./router ./router
COPY ./model ./model

RUN go build -o /Jomon -ldflags "-s -w"

## build frontend
FROM node:13.12.0-alpine as client-build
WORKDIR /github.com/traPtitech/Jomon/client
COPY ./client/package.json ./client/package-lock.json ./
RUN npm ci
COPY ./client .
RUN npm run build

## run

FROM alpine:3.9
ENV TZ Asia/Tokyo

RUN apk --update --no-cache add tzdata \
  && cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && apk del tzdata
RUN apk --update --no-cache add ca-certificates \
  && update-ca-certificates \
  && rm -rf /usr/share/ca-certificates /etc/ssl/certs

WORKDIR /app
COPY --from=server-build /Jomon ./
COPY --from=client-build /github.com/traPtitech/Jomon/client/dist ./client/dist/

ENTRYPOINT ./Jomon
