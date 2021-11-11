FROM ruby:2.3.1

ADD ./ /app
WORKDIR /app

RUN bundle install

ENTRYPOINT ["bundle", "exec", "ruby", "brain.rb"]
CMD ["1000", "5000"]
