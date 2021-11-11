FROM golang:1.16-alpine AS builder
RUN apk --no-cache add git
WORKDIR /build/
COPY . /build/
RUN go build

FROM alpine:latest
WORKDIR /app/
COPY --from=builder /build/Anrop-Squad /app/squad
CMD /app/squad
