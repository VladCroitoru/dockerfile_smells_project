FROM customercentrix/ubuntu

# Redis 2.8

RUN  date -u +"%Y-%m-%d %H:%M:%S" && cd /tmp \
  && date -u +"%Y-%m-%d %H:%M:%S" && wget http://download.redis.io/releases/redis-2.8.17.tar.gz \
  && date -u +"%Y-%m-%d %H:%M:%S" && tar xvzf redis-2.8.17.tar.gz \
  && date -u +"%Y-%m-%d %H:%M:%S" && cd redis-2.8.17 \
  && date -u +"%Y-%m-%d %H:%M:%S" && make \
  && date -u +"%Y-%m-%d %H:%M:%S" && make install \
  && date -u +"%Y-%m-%d %H:%M:%S" && cp -f src/redis-sentinel /usr/local/bin \
  && date -u +"%Y-%m-%d %H:%M:%S" && mkdir -p /etc/redis \
  && date -u +"%Y-%m-%d %H:%M:%S" && cp -f *.conf /etc/redis \
  && date -u +"%Y-%m-%d %H:%M:%S" && rm -rf /tmp/redis-2.8.17* \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(bind .*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(daemonize .*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(dir .*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(save 900 1.*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(save 300 10.*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(save 60 10000.*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^#\s\(requirepass .*\)$/requirepass foobared/' /etc/redis/redis.conf \
  && date -u +"%Y-%m-%d %H:%M:%S" 

CMD ["redis-server", "/etc/redis/redis.conf"]

EXPOSE 6379
