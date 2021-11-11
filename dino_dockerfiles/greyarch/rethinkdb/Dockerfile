FROM alpine:edge

RUN echo http://nl.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories; \
    apk add --update --no-cache rethinkdb

VOLUME ["/data"]

WORKDIR /data

EXPOSE 28015 29015 8080

ENTRYPOINT ["rethinkdb"]

CMD ["--bind", "all"]
