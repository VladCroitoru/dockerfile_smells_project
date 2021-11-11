# Build latest registry
FROM golang:1.9 as builder
RUN go get github.com/docker/distribution/cmd/registry
WORKDIR /go/src/github.com/docker/distribution/cmd/registry
RUN CGO_ENABLED=0 go build -o /registry .

FROM golang:1.9 as app
WORKDIR /go/src/github.com/uphy/registry-garbage-collector
COPY . .
RUN CGO_ENABLED=0 go build -o /app .

# Create image
FROM alpine:3.4
RUN set -ex \
    && apk add --no-cache ca-certificates apache2-utils
COPY --from=builder /registry /bin/registry
COPY --from=app /app /bin/app
RUN chmod +x /bin/registry /bin/app
RUN mkdir -p /var/lib/registry
COPY config.yml /etc/docker/registry/config.yml

ENTRYPOINT [ "/bin/app" ]
CMD [ "run" ]
