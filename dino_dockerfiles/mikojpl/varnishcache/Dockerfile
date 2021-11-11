FROM debian:stretch

LABEL maintainer="mikoj@mynwt.eu"

ENV DEBIAN_FRONTEND noninteractive

RUN \
    apt-get update && \
    apt-get -y install apt-transport-https curl gnupg psmisc && \
    curl -L https://packagecloud.io/varnishcache/varnish64/gpgkey | apt-key add - && \
    echo 'deb https://packagecloud.io/varnishcache/varnish64/debian/ stretch main' > /etc/apt/sources.list.d/varnishcache_varnish64.list && \
    echo 'deb-src https://packagecloud.io/varnishcache/varnish64/debian/ stretch main' >> /etc/apt/sources.list.d/varnishcache_varnish64.list && \
    apt-get update

RUN \
    apt-get -y install varnish=6.4.0-1~stretch && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /

ADD start_varnishd.sh /start.sh

ENV VARNISH_MALLOC '256m'
ENV VARNISH_LOG 1
ENV VARNISH_LOG_FORMAT '%h %l %u %t "%r" %s %b "%{Referer}i" "%{User-agent}i" %{Varnish:hitmiss}x'

RUN ln -sf /dev/stdout /var/log/varnish/access.log

EXPOSE 80 6082

RUN chmod +x /start.sh
# Start the varnishd
ENTRYPOINT ["./start.sh"]
