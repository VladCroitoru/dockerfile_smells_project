FROM ruby:2.3.3

ENV MESSAGE="default message"

WORKDIR /hello
COPY . /hello

RUN bundle install
EXPOSE 8080

# ruby app.rb -p 8080 -o 0.0.0.0
CMD ["ruby", "app.rb", "-p", "8080", "-o", "0.0.0.0"]

