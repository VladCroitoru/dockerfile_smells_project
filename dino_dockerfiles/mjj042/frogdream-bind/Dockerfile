FROM        mjj042/frogdream-base
MAINTAINER  Matt Jackson <mjj@frogdream.net>

# Borrowed ideas from
# xFROM sameersbn/ubuntu:14.04.20141218
# xMAINTAINER sameer@damagehead.com

RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \
 && apt-get update \
 && apt-get install -y bind9 \
 && rm -rf /var/lib/apt/lists/* # 20140918

ADD start /start
RUN chmod 755 /start

EXPOSE      53/udp
VOLUME ["/data"]
CMD ["/start"]
