FROM ruby:2.7-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    git

WORKDIR /home/jekyll

COPY Gemfile Gemfile.lock ./
RUN bundle install

CMD ["bundle", "exec", "jekyll", "serve", "--drafts", "--host", "0.0.0.0"]
EXPOSE 4000
