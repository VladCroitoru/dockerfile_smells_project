# syntax=docker/dockerfile:1.3

FROM golang:1.17 AS build

RUN mkdir -p /src/tjts
WORKDIR /src/tjts

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN --mount=type=cache,target=/root/.cache/go-build go install ./...

FROM ubuntu:focal

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/tmp" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid 1000 \
    app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y sqlite3 curl iputils-ping

COPY --from=build /go/bin/tjts /usr/bin/tjts

ENTRYPOINT ["/usr/bin/tjts"]
