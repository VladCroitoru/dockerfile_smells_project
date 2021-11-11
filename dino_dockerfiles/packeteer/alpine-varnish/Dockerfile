FROM alpine

MAINTAINER packeteer <packeteer@gmail.com>

RUN apk add --no-cache varnish

EXPOSE 8080

ENTRYPOINT ["/usr/sbin/varnishd"]
CMD ["-F", "-u", "varnish", "-f", "$VCL_CONFIG", "-s", "malloc", "$CACHE_SIZE", "$VARNISHD_PARAMS"]
