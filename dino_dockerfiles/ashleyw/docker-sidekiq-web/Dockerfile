FROM ruby:2.3.1

ADD Gemfile* /sidekiq/
WORKDIR /sidekiq
RUN bundle install

ADD config.ru /sidekiq/

EXPOSE 3030
ENTRYPOINT []
CMD rackup config.ru -o 0.0.0.0 -p 3030 -q
