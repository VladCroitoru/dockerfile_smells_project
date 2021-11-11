FROM alpine
LABEL MAINTAINER="vpn@ifree.net"


# See http://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Advanced_APK_Usage
RUN apk update && apk upgrade && apk add --no-cache strongswan


# Strongswan Configuration
ADD ./vpn_config/ipsec.conf /etc/ipsec.conf
ADD ./vpn_config/strongswan.conf /etc/strongswan.conf

# Apps
ADD init.sh /usr/bin/init

# Web
#ADD web /www
#VOLUME /www

ENV PROFILE StrongSwan
ENV PSK   asdfjkl

EXPOSE 500/udp 4500/udp

CMD /usr/bin/init
