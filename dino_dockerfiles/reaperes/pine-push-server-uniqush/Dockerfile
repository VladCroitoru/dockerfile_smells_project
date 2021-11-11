FROM dockerfile/ubuntu
MAINTAINER namhoon(emerald105@hanmail.net)

# Install redis-server
RUN \
  cd /tmp && \
  wget http://download.redis.io/redis-stable.tar.gz && \
  tar xvzf redis-stable.tar.gz && \
  cd redis-stable && \
  make && \
  make install && \
  cp -f src/redis-sentinel /usr/local/bin && \
  mkdir -p /etc/redis && \
  cp -f *.conf /etc/redis && \
  rm -rf /tmp/redis-stable* && \
  sed -i 's/^\(daemonize .*\)$/daemonize yes/' /etc/redis/redis.conf && \
  sed -i 's/^# \(bind .*\)$/\1/' /etc/redis/redis.conf && \
  sed -i 's/^\(dir .*\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \
  sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf && \
  sed -i 's/^\(port .*\)$/port 8521/' /etc/redis/redis.conf
# sed -i 's/^\(logfile .*\)$/# \1/' /etc/redis/redis.conf && \ # logging off

# Install uniqush-push
RUN \
  cd /tmp && \
  wget http://uniqush.org/downloads/uniqush-push_1.5.2_x86_64.tar.gz && \
  tar xvzf uniqush-push_1.5.2_x86_64.tar.gz && \
  cd uniqush-push_1.5.2_x86_64 && \
  mkdir -p /etc/uniqush && \
  cp -f uniqush-push /usr/local/bin && \
  cp -f uniqush-push.conf /etc/uniqush && \
  rm -rf /tmp/uniqush-push_1.5.2_x86_64* && \
  sed -i 's/^\(port.*\)$/port=8521/' /etc/uniqush/uniqush-push.conf && \
  sed -i 's/^\(logfile.*\)$/logfile=\/data/' /etc/uniqush/uniqush-push.conf && \
  sed -i 's/^\(addr.*\)$/addr=0.0.0.0:8520/' /etc/uniqush/uniqush-push.conf



ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

VOLUME ["/data"]

CMD ["/start.sh"]

EXPOSE 8520
