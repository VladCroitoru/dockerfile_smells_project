FROM ubuntu:latest
MAINTAINER Ioannis Angelakopoulos <ioagel@gmail.com>

#Upgrade system
RUN apt-get update && apt-get upgrade -y && apt-get clean

#install deluge
RUN apt-get install -qy deluged deluge-web supervisor && \
    apt-get clean

RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#set timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Athens /etc/localtime
# Add user and group media
RUN groupadd -g 10000 media
RUN useradd -m -d /var/lib/deluge -s /bin/bash -u 10000 -g 10000 media

VOLUME /var/lib/deluge

# torrent port
EXPOSE 55100
EXPOSE 55100/udp
# WebUI
EXPOSE 8112

CMD ["/usr/bin/supervisord"]
