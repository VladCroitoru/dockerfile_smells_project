FROM ruby

ENTRYPOINT ["bundle", "exec", "foreman", "start"]
EXPOSE 5000
EXPOSE 5100

WORKDIR /app
RUN gem install --no-rdoc --no-ri bundler

COPY Gemfile Gemfile.lock ./
RUN bundle

COPY . ./
