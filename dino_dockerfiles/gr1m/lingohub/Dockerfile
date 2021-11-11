FROM ruby:2.5

RUN gem install lingohub

COPY ./docker-entrypoint /usr/local/bin/
RUN mkdir /root/.lingohub
RUN mkdir /app
WORKDIR /app

ENTRYPOINT ["docker-entrypoint"]
CMD ["lingohub"]
