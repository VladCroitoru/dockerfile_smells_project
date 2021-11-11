FROM centos:7

MAINTAINER Aleksandr Lykhouzov <lykhouzov@gmail.com>

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
# Install Redis
&& yum -y update && yum install -y redis
# && sed -i 's/# unixsocket \/tmp\/redis.sock/unixsocket \/var\/run\/redis\/redis.sock/g' /etc/redis.conf \
# && sed -i 's/# unixsocketperm 700/unixsocketperm 777/g' /etc/redis.conf

EXPOSE 6379
CMD [ "redis-server","--daemonize","no","--loglevel","verbose"]
