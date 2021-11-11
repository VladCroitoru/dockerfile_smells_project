FROM greatbsky/centos7
MAINTAINER architect.bian
LABEL name="redis" license="GPLv2" build-date="20161123"

ENV redis_VERSION 3.2.5

RUN yum clean all && yum update -y
COPY startup.sh /data/env/redis/startup
RUN groupadd -r redis && useradd -r -g redis redis && mkdir -p /data/env/redis/db && chown redis:redis /data/env/redis && chmod +x /data/env/redis/startup && cd /data/softs && wget -O redis.tar.gz http://download.redis.io/releases/redis-$redis_VERSION.tar.gz && tar -zxf redis.tar.gz && cd redis-$redis_VERSION && make && cp /data/softs/redis-$redis_VERSION/src/redis-server /usr/bin/redis-server && cp /data/softs/redis-$redis_VERSION/src/redis-cli /usr/bin/redis-cli && sed 's/bind 127.0.0.1/#bind 127.0.0.1/' /data/softs/redis-$redis_VERSION/redis.conf | sed 's/protected-mode yes/protected-mode no/' > /data/env/redis/redis.conf && echo 'vm.overcommit_memory = 1' >> /etc/sysctl.conf

USER root
WORKDIR /data/env/redis/db
EXPOSE 6379

CMD ["/data/env/redis/startup"]
