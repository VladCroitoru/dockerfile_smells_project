FROM ruby:2.5.1

WORKDIR /app

COPY Gemfile Gemfile.lock ./
RUN bundle install --without development
ADD . /app

EXPOSE 8080

CMD unicorn
