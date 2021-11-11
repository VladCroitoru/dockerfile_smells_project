FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends\
    build-essential\
    wget\
    ruby\
    git\
    libevent-dev\
    stunnel4\
    net-tools\
    && gem install redis \
    && wget -O redis.tar.gz http://download.redis.io/releases/redis-3.2.0.tar.gz \
    && mkdir -p /usr/src/redis \
    && tar -xzf redis.tar.gz -C /usr/src/redis --strip-components=1 \
    && rm redis.tar.gz \
    && make -C /usr/src/redis \
    && make -C /usr/src/redis install \
    && rm -rf /usr/src/redis  \
    && git clone git://github.com/nicolasff/webdis.git \
    && cd webdis \
    && make \
    && make install \
    && apt-get purge -y --auto-remove build-essential git gcc make libc6-dev \
    && rm -rf /var/lib/apt/lists/* 

RUN mkdir -p /opt/config

EXPOSE 6379

VOLUME /opt/redisdb 
VOLUME /opt/config

COPY webdis.json stunnel.conf redis.* chain-of-trust.pem /opt/config/
COPY redis-trib.rb /usr/local/bin/
COPY dotbashrc /root/.bashrc
COPY welcome.ascii /etc/

CMD ["/usr/local/bin/redis-server","/opt/config/redis.conf"]
