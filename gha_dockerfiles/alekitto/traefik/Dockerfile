FROM alpine:3.11
RUN apk --no-cache add ca-certificates tzdata wget
COPY script/ca-certificates.crt /etc/ssl/certs/
COPY dist/traefik /
EXPOSE 80
VOLUME ["/tmp"]
ENTRYPOINT ["/traefik"]
