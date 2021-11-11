FROM ruby
RUN mkdir /app
WORKDIR /app
COPY Gemfile Gemfile.lock /app/
RUN bundle
COPY ./ ./
CMD ruby app.rb
