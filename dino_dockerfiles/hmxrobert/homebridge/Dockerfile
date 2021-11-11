FROM archlinuxjp/archlinux:2017.01.15
MAINTAINER hmxrobert

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm nodejs npm python2 make gcc avahi nss-mdns

RUN npm install -g node-gyp
RUN npm install -g homebridge
RUN npm install -g homebridge-irkit

ADD init.sh /
RUN chmod +x /init.sh

ADD nsswitch.conf /etc/

EXPOSE 5353/udp 51826

VOLUME /mnt/homebridge/

CMD ["/init.sh"]
