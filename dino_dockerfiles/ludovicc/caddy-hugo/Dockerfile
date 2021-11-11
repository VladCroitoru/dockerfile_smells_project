FROM alpine:3.3
MAINTAINER Ludovic Claude <ludovic.claude@laposte.net>

LABEL caddy_version="0.8.2" architecture="amd64"

RUN apk add --update openssh-client git tar

RUN curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
      "https://caddyserver.com/download/build?os=linux&arch=amd64&features=hugo%2Cgit%2Crealip%2Csearch" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
 && chmod 0755 /usr/bin/caddy \
 && /usr/bin/caddy -version

EXPOSE 80 443 2015
VOLUME /srv
WORKDIR /srv

COPY caddy-hugo.sh /caddy-hugo.sh
RUN chmod +x /caddy-hugo.sh
ENTRYPOINT ["/bin/sh", "-c", "/caddy-hugo.sh"]
CMD ["-conf", "/srv/Caddyfile"]
