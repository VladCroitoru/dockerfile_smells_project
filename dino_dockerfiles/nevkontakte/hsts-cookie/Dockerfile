FROM golang:1.8-alpine AS go-builder
WORKDIR /app
RUN apk add --update git
RUN go get github.com/constabulary/gb/...
COPY ./vendor ./vendor
COPY ./src ./src
RUN gb build

FROM alpine:latest
RUN apk add --update ca-certificates
WORKDIR /app
COPY --from=go-builder /app/bin/server /usr/local/bin/hsts-cookie
VOLUME /srv
EXPOSE 80 443
ENTRYPOINT ["hsts-cookie", "-acme_dir=/srv/acme-cache"]

