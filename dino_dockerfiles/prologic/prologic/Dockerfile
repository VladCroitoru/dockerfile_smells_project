# Build
FROM golang:alpine AS build

RUN apk add --update git build-base && \
    rm -rf /var/cache/apk/*

RUN go get github.com/gohugoio/hugo

# Runtime
FROM alpine
COPY . /var/www
COPY --from=build /go/bin/hugo /hugo
WORKDIR /var/www

EXPOSE 1313/tcp

ENTRYPOINT ["/hugo"]
CMD ["server", "--bind", "0.0.0.0"]
