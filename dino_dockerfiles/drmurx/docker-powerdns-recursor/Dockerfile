FROM alpine:3.7

RUN apk add --update --no-cache pdns-recursor

EXPOSE 53/udp

ENTRYPOINT ["/usr/sbin/pdns_recursor", "--local-address=0.0.0.0:53", "--allow-from=0.0.0.0/0", "--daemon=no"]
