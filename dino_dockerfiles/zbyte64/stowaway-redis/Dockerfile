FROM phusion/baseimage
MAINTAINER Jason Kraus "jason@montagable.com"
RUN	echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get install -y redis-server
RUN mkdir /etc/service/redis
ADD ./run.sh /etc/service/redis/run
RUN chmod +x /etc/service/redis/run
ADD ./redis.conf /etc/redis/redis.conf

EXPOSE 6379

CMD /sbin/my_init

RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

