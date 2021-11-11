FROM golang:1.14 AS build

ENV GO111MODULE=on
ENV GOFLAGS=-mod=vendor
ENV CGO_ENABLED=0

ENV APP_HOME /go/src/splend-api

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY . .

RUN go mod download
RUN go mod vendor
RUN go mod verify
RUN go build -o splend-api cmd/splend-api/main.go

FROM alpine:latest

ENV APP_USER splend
RUN addgroup -S $APP_USER && adduser -S -G $APP_USER $APP_USER
USER $APP_USER

COPY etc/splend/splend-api.prod.yaml /etc/splend/splend-api.yaml
COPY --from=build /go/src/splend-api/splend-api /usr/bin/

CMD ["splend-api"]
