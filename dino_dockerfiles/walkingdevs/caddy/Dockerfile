FROM alpine:3.8

RUN ln -s /root/.caddy /caddy

VOLUME /caddy

EXPOSE 80 443

ENTRYPOINT ["start-caddy"]

RUN apk update && \
    apk upgrade && \
    apk add caddy && \
    rm -rf /var/cache/apk/*

COPY start-caddy /bin