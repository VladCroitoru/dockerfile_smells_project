FROM golang:1.10-alpine as builder
ENV VERSION=${VERSION:-"0.11.0"}
RUN apk add --no-cache git gcc musl-dev
RUN git clone https://github.com/mholt/caddy -b "v$VERSION" /go/src/github.com/mholt/caddy
RUN go get -u github.com/caddyserver/builds
RUN go get github.com/caddyserver/dnsproviders/googlecloud/
RUN sed '/This is where other plugins get plugged in/a_ \"github.com/caddyserver/dnsproviders/googlecloud\"' -i /go/src/github.com/mholt/caddy/caddy/caddymain/run.go
RUN cat /go/src/github.com/mholt/caddy/caddy/caddymain/run.go


# Build
RUN cd /go/src/github.com/mholt/caddy/caddy \
    && go run build.go -goos=linux -goarch=amd64 \
    && mv caddy /

# validate install
RUN /caddy -version && /caddy -plugins


FROM alpine:3.8

ENV ACME_AGREE="true"

COPY --from=builder /caddy /usr/bin/caddy

RUN apk add --no-cache ca-certificates
EXPOSE 80 443
VOLUME /root/.caddy /srv
WORKDIR /srv

COPY Caddyfile Caddyfile.template /etc/
COPY caddy_start.sh caddy_generate_single.sh /

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/caddy_start.sh"]

