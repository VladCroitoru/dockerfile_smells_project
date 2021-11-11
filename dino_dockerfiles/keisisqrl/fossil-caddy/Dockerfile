FROM alpine:3.6

ENV FOSSILVER 2.4
ENV CADDYPATH /fossil-data
ENV CA_URI https://acme-staging.api.letsencrypt.org/directory

RUN apk add --no-cache curl s6 ca-certificates \
    && curl https://www.fossil-scm.org/index.html/uv/fossil-linux-x64-${FOSSILVER}.tar.gz \
    | tar xzf - \
    && curl -L 'https://caddyserver.com/download/linux/amd64?plugins=http.cgi&license=personal' \
    | tar xzf - caddy \
    && chmod +x fossil caddy \
    && mv fossil caddy /usr/bin \
    && apk del curl

ADD service /service

VOLUME /fossil-data

EXPOSE 80 443

ENTRYPOINT ["s6-svscan","/service"]
