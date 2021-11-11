FROM golang:1.17-alpine as builder
RUN apk add --no-cache git make
ENV GOOS=linux
ENV CGO_ENABLED=0
COPY . /src
WORKDIR /src
RUN make test
RUN make alpine

FROM alpine:3.14
RUN apk add --no-cache ca-certificates
WORKDIR /app
COPY --from=builder /src/bin/deployment-event-relays /app/deployment-event-relays
CMD ["/app/deployment-event-relays"]
