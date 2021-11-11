from ubuntu:12.04
maintainer Shipyard Project "http://shipyard-project.com"
run apt-get update
run apt-get install -y make gcc wget
run wget http://download.redis.io/releases/redis-2.6.16.tar.gz -O /tmp/redis.tar.gz
run (cd /tmp && tar zxf redis.tar.gz && cd redis-* && make install && cp redis.conf sentinel.conf /etc/)
run rm -rf /tmp/*
expose 6379
volume /var/lib/redis
workdir /var/lib/redis
entrypoint ["/usr/local/bin/redis-server"]
cmd ["/etc/redis.conf"]
