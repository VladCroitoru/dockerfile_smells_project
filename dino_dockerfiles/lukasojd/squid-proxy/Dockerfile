FROM lukasojd/docker-gen:latest

MAINTAINER Lukáš Kříž <lukasojd@gmail.com>

RUN apt-get update
RUN apt-get install -y squid3 dnsmasq

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /app/
WORKDIR /app/

COPY containers.conf.tmpl /app/
COPY run.sh /run.sh
COPY squid.conf /etc/squid3/squid.conf
COPY dnsmasq.conf /etc/dnsmasq.conf

EXPOSE 3128 53/tcp 53/udp

VOLUME ["/etc/dnsmasq.d/"]
CMD ["/run.sh"]
