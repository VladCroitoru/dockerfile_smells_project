FROM debian:jessie
MAINTAINER "Niklas Nihlén" <niklas.nihlen@viaplay.ccom>

RUN apt-get update && apt-get install -y curl python --no-install-recommends && rm -r /var/lib/apt/lists/*
RUN curl http://repo.varnish-cache.org/GPG-key.txt | apt-key add --
RUN echo "deb http://repo.varnish-cache.org/debian/ jessie varnish-4.1" >> /etc/apt/sources.list.d/varnish-cache.list
RUN apt-get update && apt-get install -y varnish --no-install-recommends && rm -r /var/lib/apt/lists/*
#RUN mkdir -p /etc/varnish/conf.d/


# Make our custom VCLs available on the container
ADD default.vcl /etc/varnish/default.vcl
ADD default.vcl /default.vcl

# ENV VARNISH_BACKEND_PORT 3000
# ENV VARNISH_BACKEND_IP 192.168.99.100
# ENV VARNISH_PORT 80

# Expose port 80
# EXPOSE 80

# Expose volumes to be able to use data containers
VOLUME ["/var/lib/varnish", "/etc/varnish"]

ADD start.sh /start.sh
CMD ["/start.sh"]
