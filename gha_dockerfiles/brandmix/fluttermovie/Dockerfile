#Deploy SPA
FROM alpine:latest

RUN apk add --no-cache openssh-client tar curl
RUN curl --silent -o - "https://caddyserver.com/api/download?os=linux&arch=amd64" > /usr/bin/caddy
RUN chmod 0755 /usr/bin/caddy

COPY web/build /srv/www/
COPY Caddyfile /etc/

EXPOSE 80 443
WORKDIR /srv/www
ENTRYPOINT ["/usr/bin/caddy","run","-config","/etc/Caddyfile"]
