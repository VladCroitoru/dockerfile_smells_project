FROM phusion/baseimage
MAINTAINER manu <manu.bocquet@gmail.com>

ENV APTLIST="squid3 gawk wget" 
ENV SYSLOG_ADDR="192.168.1.5:514"

# install main packages
RUN apt-get update -q && \
apt-get install $APTLIST -qy && \

# cleanup
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl -o /usr/bin/scalar.awk https://raw.githubusercontent.com/horsley/squid-log-analyse/master/scalar.awk
RUN chmod 755 /usr/bin/scalar.awk

RUN mkdir /config
RUN mkdir /etc/service/squid3
ADD ./init.sh /etc/service/squid3/run
RUN chmod 755 /etc/service/squid3/run

# Export 
VOLUME [ "/var/log/squid" ]
VOLUME [ "/config" ]

ADD ./proxy_cron /var/spool/cron/crontabs/root
ADD ./proxy_cron.sh /root/proxy_cron.sh
RUN chmod 755 /root/proxy_cron.sh

# ports and volumes
EXPOSE 3128

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
