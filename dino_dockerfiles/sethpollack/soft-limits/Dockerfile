FROM beenverifiedinc/glide AS vendor
WORKDIR /go/src/github.com/sethpollack/soft-limits
COPY glide.yaml glide.lock ./
RUN glide install --strip-vendor

FROM golang:1.8-alpine AS build
RUN apk --no-cache update && \
  apk --no-cache add make ca-certificates git && \
  rm -rf /var/cache/apk/*
WORKDIR /go/src/github.com/sethpollack/soft-limits
COPY . ./
COPY --from=vendor /go/src/github.com/sethpollack/soft-limits/vendor ./vendor
RUN	CGO_ENABLED=0 GOOS=linux go build -installsuffix cgo -o bin/soft-limits

FROM scratch AS soft-limits
LABEL maintainer="Seth Pollack <seth@sethpollack.net>"
COPY --from=build /etc/ssl/certs/ /etc/ssl/certs/
COPY --from=build /go/src/github.com/sethpollack/soft-limits/bin/soft-limits /usr/local/bin/soft-limits
ENTRYPOINT ["/usr/local/bin/soft-limits"]
CMD ["--help"]
