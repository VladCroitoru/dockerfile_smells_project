FROM ruby:2.3
COPY . /app
WORKDIR /app
RUN bundle install
ENTRYPOINT ["./generate-domain.rb"]
