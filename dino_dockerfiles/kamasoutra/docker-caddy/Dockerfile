FROM alpine:latest

LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \
      description="Docker container with Caddy server" \
      version="1.0"

RUN apk add --update curl bash && \
    mkdir /dl && \
    curl https://getcaddy.com | bash -s personal http.filemanager,http.git,http.ipfilter,http.login

EXPOSE 80 443

CMD ["/usr/local/bin/caddy", "--conf", "/etc/Caddyfile", "--log", "stdout"]
