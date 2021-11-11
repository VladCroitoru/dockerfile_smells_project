FROM debian:jessie

RUN apt-get update && \
    apt-get install -y varnish

COPY mediawiki.vcl /etc/varnish/mediawiki.vcl
COPY configure.sh /usr/local/bin/configure-varnish
RUN chmod +x /usr/local/bin/configure-varnish

ENV BACKEND_HOST=web
ENV BACKEND_PORT=80
ENV VCL=/etc/varnish/mediawiki.vcl

EXPOSE 80

CMD configure-varnish && \
    varnishd -a :80 -f /etc/varnish/mediawiki.vcl && \
    sleep 1 && \
    varnishncsa