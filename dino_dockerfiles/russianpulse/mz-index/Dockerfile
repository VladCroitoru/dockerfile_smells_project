FROM ruby:2.4.1

RUN mkdir /app
WORKDIR /app

COPY Gemfile* /app/
RUN bundle install

COPY . /app/

EXPOSE 80

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["web"]
