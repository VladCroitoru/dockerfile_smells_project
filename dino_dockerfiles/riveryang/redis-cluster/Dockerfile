# Redis Cluster for CentOS 7
# Version 3.2.4

FROM centos:7
MAINTAINER RiverYang "comicme_yanghe@icloud.com"

RUN yum update -y 
RUN yum install -y wget gcc make which

RUN mkdir -p /data/redis-cluster/configs

RUN cd /usr/local/src && \
wget http://download.redis.io/releases/redis-3.2.4.tar.gz && \
tar -zxvf redis-3.2.4.tar.gz && \
cd redis-3.2.4 && make && make install && \
cp src/redis-trib.rb /usr/local/bin && \
cp utils/redis_init_script.tpl /data/redis-cluster && \
redis-server -v && cd .. && rm -rf redis*

COPY cluster_instance.sh /data/redis-cluster

COPY redis.conf /data/redis-cluster

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh && chmod +x /data/redis-cluster/cluster_instance.sh

ENV REDIS_PORT 7000
ENV REDIS_CLUSTER_PORT 17000

EXPOSE $REDIS_PORT $REDIS_CLUSTER_PORT

ENTRYPOINT ["/entrypoint.sh"]
