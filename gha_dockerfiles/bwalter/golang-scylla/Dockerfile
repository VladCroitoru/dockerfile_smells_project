# stage 1: build

FROM golang:1.17-alpine as builder

RUN apk add make

WORKDIR /tmp/hello-build

COPY go.mod go.sum ./
COPY . .

RUN make build
RUN make unit-tests

# stage 2: run

FROM alpine:3.14

COPY --from=builder /tmp/hello-build/bin/hello /app/hello

EXPOSE 3001
ENTRYPOINT ["/app/hello"]
