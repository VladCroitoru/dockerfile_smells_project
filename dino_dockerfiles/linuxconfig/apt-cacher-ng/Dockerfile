FROM debian:8

MAINTAINER Lubos Rendek <web@linuxconfig.org>

RUN apt-get update
RUN apt-get install -y apt-cacher-ng

EXPOSE 3142

CMD ["/usr/sbin/apt-cacher-ng", "ForeGround=1", "CacheDir: /var/cache/apt-cacher-ng"]
