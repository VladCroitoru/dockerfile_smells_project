FROM centos:latest
MAINTAINER Matej Kramny <matej@matej.me>

RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
RUN yum install -y gcc-c++ make tar

RUN curl -L wget http://download.redis.io/releases/redis-2.8.11.tar.gz | tar xzf -
WORKDIR redis-2.8.11
RUN make
RUN make install

WORKDIR ..
RUN rm -rf redis-2.8.11

ADD redis.conf /etc/redis.conf
ADD start.sh /usr/local/bin/redis_start
RUN chmod +x /usr/local/bin/redis_start

EXPOSE 6379

CMD ["/usr/local/bin/redis_start"]
