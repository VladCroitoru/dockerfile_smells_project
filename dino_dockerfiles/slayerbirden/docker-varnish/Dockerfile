FROM alpine:3.6

MAINTAINER Oleg Kulik "okulik@gorillagroup.com"

RUN apk update && apk add varnish

# main varnish port + admin service port
EXPOSE 80 6082

COPY start.sh /

ENTRYPOINT ["/start.sh"]

ENV VARNISHD_FLAGS "-f /etc/varnish/default.vcl"

CMD ["varnishlog"]
