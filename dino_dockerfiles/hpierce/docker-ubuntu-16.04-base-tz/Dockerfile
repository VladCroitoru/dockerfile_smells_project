#
# Base TZ Dockerfile
#
#
FROM hpierce/docker-ubuntu-16.04-base

RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/US/Eastern /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

