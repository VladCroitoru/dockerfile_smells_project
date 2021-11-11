FROM alpine:3.4
MAINTAINER David Banham <david@banham.id.au>

ARG plugins=

RUN apk add --no-cache openssh-client tar curl

RUN curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
      "https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
 && chmod 0755 /usr/bin/caddy \  
 && /usr/bin/caddy -version

EXPOSE 80 443 2015
WORKDIR /srv

RUN touch /etc/Caddyfile

ENTRYPOINT ["/usr/bin/caddy"]
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]
