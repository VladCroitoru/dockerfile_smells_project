FROM       phusion/baseimage:0.9.16
MAINTAINER Andy Bavier <acb@cs.princeton.edu>

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y ufw dnsmasq tcpdump python

### Dnsmasq setup
RUN mkdir /etc/service/dnsmasq
ADD etc/service/dnsmasq/run /etc/service/dnsmasq/
RUN mkdir /etc/service/dnsmasq-safe
ADD etc/service/dnsmasq-safe/run /etc/service/dnsmasq-safe/

### Firewall and NAT setup
RUN mkdir -p /mount
ADD etc/ufw/before.rules /mount/
ADD etc/rc.local /mount/
RUN chmod +x /mount/rc.local
RUN rm /etc/ufw/before.rules; ln -s /mount/before.rules /etc/ufw/before.rules
RUN rm /etc/rc.local; ln -s /mount/rc.local /etc/rc.local

