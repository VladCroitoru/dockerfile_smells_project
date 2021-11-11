FROM golang:1.14-alpine AS builder
RUN apk --no-cache add git
WORKDIR /build/
COPY . /build/
RUN go build

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /app/
COPY --from=builder /build/Anrop-Streams /app/streams
CMD /app/streams
