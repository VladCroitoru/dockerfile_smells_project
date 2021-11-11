FROM golang:alpine as build

# Install git and get the caddy source code
RUN apk --update add git
RUN go get github.com/mholt/caddy/caddy

# Checkout the latest stable release
WORKDIR /go/src/github.com/mholt/caddy
RUN git tag -l --sort=-creatordate | grep -v beta | head -n 1 | xargs git checkout
# Build it
WORKDIR /go/src/github.com/mholt/caddy/caddy
RUN go build

FROM alpine:latest
ENV ACME_AGREE=false

EXPOSE 80
EXPOSE 443
COPY --from=build /go/src/github.com/mholt/caddy/caddy/caddy /
RUN mkdir /config
COPY Caddyfile /config/Caddyfile
VOLUME /config

CMD ["/caddy", "-conf", "/config/Caddyfile", "-agree=true"]
