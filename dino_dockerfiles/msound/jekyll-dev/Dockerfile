FROM ruby:2.3

MAINTAINER Mani Soundararajan <mani.sound@gmail.com>

COPY resources/Gemfile /internal/

WORKDIR /internal

RUN bundle install

COPY resources/jekyll-dev.sh /internal/

VOLUME ['/usr/app/src']

EXPOSE 4000

ENTRYPOINT ["/internal/jekyll-dev.sh"]
CMD [ "serve" ]
