FROM sorah/ruby:2.4
MAINTAINER sorah

RUN mkdir -p /app

ADD Gemfile* /tmp/
ADD wifidiag.gemspec /tmp/
RUN mkdir -p /tmp/lib/wifidiag
ADD lib/wifidiag/version.rb /tmp/lib/wifidiag/version.rb
RUN cd /tmp && bundle install -j4 --path vendor/bundle --without 'development test'

WORKDIR /app
ADD . /app
RUN cp -a /tmp/.bundle /tmp/vendor /app/
RUN rm -f /app/.ruby-version

EXPOSE 8080
ENV RACK_ENV=production
WORKDIR /app
CMD ["/app/docker-sun.sh"]
