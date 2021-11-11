FROM ruby:2.4.1

COPY . /app
WORKDIR /app

ENV DATA_DIR /data
VOLUME /data

EXPOSE 80

RUN bundle install
ENTRYPOINT ["bundle", "exec"]
CMD ["app.rb", "-p", "80", "-o", "0.0.0.0"]
