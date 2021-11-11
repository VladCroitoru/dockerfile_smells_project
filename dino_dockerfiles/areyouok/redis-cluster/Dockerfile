FROM redis:4

MAINTAINER huangli <areyouok@gmail.com>

RUN apt-get update -qq && \
    apt-get install --no-install-recommends -yqq \
      net-tools ruby rubygems && \
    apt-get clean -yqq
RUN gem install redis
ADD redis-trib.rb /usr/local/bin/redis-trib.rb
COPY docker-cluster-entrypoint.sh /usr/local/bin/
COPY redisclusterconf /etc/redisclusterconf
RUN chmod +x /usr/local/bin/docker-cluster-entrypoint.sh /usr/local/bin/redis-trib.rb
ENTRYPOINT ["docker-cluster-entrypoint.sh"]

EXPOSE 7000 7001 7002 7003 7004 7005