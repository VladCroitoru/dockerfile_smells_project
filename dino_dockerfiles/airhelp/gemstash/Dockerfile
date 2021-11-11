FROM ruby:2.6

ENV RACK_ENV production
ENV GEMSTASH_VERSION=2.1.0

EXPOSE 9292

RUN gem install gemstash --version $GEMSTASH_VERSION

CMD ["gemstash", "start", "--no-daemonize"]
