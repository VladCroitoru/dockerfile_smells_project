FROM ubuntu

MAINTAINER Alexander Gorokhov <sashgorokhov@gmail.com>

EXPOSE 3142
VOLUME ["/var/cache/apt-cacher-ng"]

RUN apt-get update && apt-get install -y apt-cacher-ng
CMD chmod 777 /var/cache/apt-cacher-ng && /etc/init.d/apt-cacher-ng start && tail -f /var/log/apt-cacher-ng/*

