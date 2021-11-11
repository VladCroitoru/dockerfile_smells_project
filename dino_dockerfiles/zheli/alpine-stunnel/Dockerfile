FROM alpine:edge

RUN apk add --no-cache stunnel libressl \
        && mkdir -p /var/run/stunnel \
        && chown stunnel:stunnel -R /var/run/stunnel

CMD ["/usr/bin/stunnel"]
