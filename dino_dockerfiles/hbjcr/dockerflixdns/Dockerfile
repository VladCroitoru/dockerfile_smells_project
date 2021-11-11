FROM ubuntu
MAINTAINER Hector Bejarano
# Detailed explanation: https://blog.heckel.xyz/2013/07/18/how-to-dns-spoofing-with-a-simple-dns-server-using-dnsmasq/

RUN apt-get update && apt-get install -y dnsmasq-base dnsutils && apt-get clean

RUN mkdir /config

RUN echo "no-dhcp-interface=" > /config/dnsmasq.conf
RUN echo "server=8.8.8.8" >> /config/dnsmasq.conf

RUN echo "no-hosts" >> /config/dnsmasq.conf
RUN echo "addn-hosts=/config/dnsmasq.hosts" >> /config/dnsmasq.conf

RUN touch /config/dnsmasq.hosts
VOLUME /config

EXPOSE 53

CMD ["/usr/sbin/dnsmasq","-d","-C","/config/dnsmasq.conf"]
