FROM ruby:2.3.1

RUN mkdir /gemstash
RUN gem install --no-ri --no-rdoc -v 1.0.1 gemstash
COPY config.yml /gemstash/config.yml

VOLUME ["/gemstash/gem_cache"]
CMD ["gemstash", "start", "--no-daemonize", "--config-file", "/gemstash/config.yml"]
