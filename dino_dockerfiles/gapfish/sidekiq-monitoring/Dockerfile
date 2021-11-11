FROM ruby

RUN gem install rack sidekiq
COPY config.ru config.ru

EXPOSE 9292

CMD rackup config.ru --host 0.0.0.0
