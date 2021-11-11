FROM ruby:2.2.0
ENV PORT 80
ADD . /app
WORKDIR /app
RUN bundle install --path=vendor/bundle -j4
CMD bundle exec ruby app.rb -p $PORT -o 0.0.0.0
