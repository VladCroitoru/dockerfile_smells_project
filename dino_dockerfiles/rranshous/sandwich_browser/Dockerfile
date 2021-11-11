FROM ruby:2.3.3

VOLUME /data

ADD ./ /app
WORKDIR /app

RUN bundle install

ENV IMAGE_DIR=/data

ENTRYPOINT ["bundle", "exec"]
CMD ["ruby", "app.rb", "-p", "80", "-o", "0.0.0.0"]
