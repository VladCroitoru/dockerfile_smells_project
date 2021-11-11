FROM alpine:latest
MAINTAINER Philipp Hellmich <phil@hellmi.de>

ARG plugins=http.git,tls.dns.route53,http.prometheus,http.filemanager

RUN apk --no-cache add tini git openssh-client \
    && apk --no-cache add --virtual devs tar curl

RUN curl --silent --show-error --fail --location \
      --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
      "https://caddyserver.com/download/linux/amd64?plugins=${plugins}&license=personal" \
    | tar --no-same-owner -C /usr/bin/ -xz caddy \
 && chmod 0755 /usr/bin/caddy \
 && /usr/bin/caddy -version

#Remove build devs
RUN apk del devs

EXPOSE 80 443 2015
VOLUME /root/.caddy
WORKDIR /srv

ADD https://raw.githubusercontent.com/abiosoft/caddy-docker/master/Caddyfile /etc/Caddyfile
ADD https://raw.githubusercontent.com/abiosoft/caddy-docker/master/index.html /srv/index.html

ENTRYPOINT ["/sbin/tini"]

CMD ["/usr/bin/caddy", "--conf", "/etc/Caddyfile", "--log", "stdout", "-agree"]
