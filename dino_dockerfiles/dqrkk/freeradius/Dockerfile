FROM ubuntu:14.04
MAINTAINER DqRkk <romain.gitlab@gmail.com>

RUN apt-get update \
 && apt-get install -y freeradius freeradius-utils libperl5.18 perl perl-base librpc-xml-perl \
 && apt-get clean autoclean \
 && apt-get autoremove -y \
 && rm -rf /var/lib/{apt,dpkg,cache,log}/

VOLUME ["/etc/freeradius/"]

EXPOSE 1812/udp
EXPOSE 18120/udp

CMD [ "/usr/sbin/freeradius", "-f" ]
