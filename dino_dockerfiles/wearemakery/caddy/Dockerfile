FROM alpine:3.9

MAINTAINER Gyula Voros <gyula@makery.co>

ARG version=v0.11.5

RUN apk add --update ca-certificates

RUN apk add --no-cache curl \
  && curl -L --silent --show-error --fail --location https://github.com/mholt/caddy/releases/download/${version}/caddy_${version}_linux_amd64.tar.gz \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
  && /usr/bin/caddy -version \
  && apk del curl

EXPOSE 80 443

ENTRYPOINT ["/usr/bin/caddy"]
CMD ["--conf", "/etc/Caddyfile"]
