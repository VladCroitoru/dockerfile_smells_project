FROM alpine:3.6
LABEL maintainer="Marco Cotrufo <info@devncode.it>"

RUN apk add --no-cache varnish

ENV VCL_CONFIG '/etc/varnish/default.vcl'
ENV CACHE_SIZE 64m

COPY start.sh /start.sh
COPY default.vcl $VCL_CONFIG
VOLUME [ "/etc/varnish/" ]

CMD /start.sh
EXPOSE 8080