FROM alpine:3.4

RUN apk --update add postgresql s6 && \
    rm -fr /var/cache/apk/*

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

COPY etc/ /etc/

ENV DB_NAME=demo

EXPOSE 5432

ENTRYPOINT ["/init"]
