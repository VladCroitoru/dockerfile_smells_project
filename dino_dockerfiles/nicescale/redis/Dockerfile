FROM  ubuntu
# choose 6379 for redis user
RUN  groupadd redis -g 6379
RUN  useradd redis -u 6379 -g redis -M -d /var/lib/redis -s /bin/false
# install redis-server
RUN  apt-get update
RUN  DEBIAN_FRONTEND=noninteractive apt-get -y install redis-server

# listen all interfaces
RUN  sed -i -e 's/^bind.*/#bind 127.0.0.1/' -e 's/^daemon.*/#daemon yes/' /etc/redis/redis.conf
ADD  crontab /etc/crontab
ADD  . /opt/nicedocker

EXPOSE  6379
CMD  ["/opt/nicedocker/run.sh"]

