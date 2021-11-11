FROM ruby:2.3

RUN gem install puma sinatra puma-metrics

USER 1000
COPY ./ /code
WORKDIR /code

CMD ["puma", "config.ru", "-C", "puma.rb"]
