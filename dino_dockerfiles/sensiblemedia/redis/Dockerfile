FROM redis
RUN apt-get update && apt-get install -y \
    vim \
	net-tools \
	tcpdump
COPY files/redis.conf /usr/local/etc/redis/redis.conf
COPY files/motd /etc/motd
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
