FROM golang as builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
# Static build required so that we can safely copy the binary over.
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

FROM alpine:latest as essentials
RUN apk --no-cache add tzdata zip ca-certificates
WORKDIR /usr/share/zoneinfo
# -0 means no compression.  Needed because go's
# tz loader doesn't handle compressed data.
RUN zip -r -0 /zoneinfo.zip .

FROM scratch
# the program:
COPY --from=builder /app/portier /portier
# the timezone data:
ENV ZONEINFO /zoneinfo.zip
COPY --from=essentials /zoneinfo.zip /
# the tls certificates:
COPY --from=essentials /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
ENTRYPOINT ["/portier"]
