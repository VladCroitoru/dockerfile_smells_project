# Ubuntu Redis.

FROM ubuntu:14.04
MAINTAINER Thomas Quintana <thomas@bettervoice.com>

# Add the latest stable redis ppa.
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:chris-lea/redis-server

# Install.
RUN apt-get update && apt-get install -y python python-dev python-pip redis-server
RUN pip install Jinja2

# Copy template files into the container.
RUN mkdir /usr/share/redis
ADD conf/redis.conf.template /usr/share/redis/redis.conf.template
ADD conf/sentinel.conf.template /usr/share/redis/sentinel.conf.template

# Update sysctl.conf.
RUN echo "vm.overcommit_memory=1" >> /etc/sysctl.conf

# Copy and register the sentinel sysv script.
ADD sysv/sentinel-server /etc/init.d/sentinel-server
RUN chmod +x /etc/init.d/sentinel-server
RUN update-rc.d -f sentinel-server defaults

# Copy the start-redis script into the container.
ADD bin/start-redis /usr/bin/start-redis
RUN chmod +x /usr/bin/start-redis

# Open the container up to the world.
EXPOSE 6379/tcp
EXPOSE 26379/tcp

# Start the redis cluster.
CMD start-redis
