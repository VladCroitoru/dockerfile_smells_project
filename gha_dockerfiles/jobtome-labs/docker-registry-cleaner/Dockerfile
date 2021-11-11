#
# App builder
#
FROM golang:1.16.6-alpine AS builder

WORKDIR /build

ADD . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o cleaner ./cmd/cleaner


#
# Certs update
#
FROM alpine:3.13 AS certs

RUN apk --update add ca-certificates

#
# Minimal image
#
FROM scratch AS minimal

ENV PATH=/bin
COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /build/cleaner /bin/cleaner

ENTRYPOINT ["cleaner"]

#
# Main image
#
FROM alpine:3.13 AS main

COPY --from=certs /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /build/cleaner /bin/cleaner
