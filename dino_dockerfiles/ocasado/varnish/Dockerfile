FROM alpine:3.5

MAINTAINER Nils Jørgen Mittet <njmittet@gmail.com>

RUN apk add --update varnish && rm -rf /var/cache/apk/*

ENV VCL_CONFIG '/etc/varnish/default.vcl'
ENV CACHE_SIZE 64m

COPY start.sh /start.sh
COPY default.vcl $VCL_CONFIG

CMD /start.sh
EXPOSE 8080
