FROM ubuntu
RUN groupadd memcache -g 11211
RUN useradd memcache -u 11211 -g memcache -M -d /nonexistent -s /bin/false
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install memcached
RUN mkdir -p /var/log/supervisor
ADD ./memcached.cfg /etc/memcached/memcached.cfg
ADD . /opt/nicedocker
EXPOSE 11211
CMD ["/opt/nicedocker/run.sh"]
