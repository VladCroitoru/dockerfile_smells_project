FROM ruby:2.4.1

MAINTAINER Sergei O. Udalov <sergei.udalov@gmail.com>

ENV HOME /root

RUN mkdir -p /app
WORKDIR /app

ADD Gemfile* ./
RUN bundle install

ADD . ./

EXPOSE 80

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["web"]
