FROM ruby:2.3.3

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \
 && apt-get install -y nodejs

RUN apt-get update && apt-get install -y \
    cmake \
 && rm -rf /var/lib/apt/lists/*

RUN bundle config --global frozen 1

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

ENV PORT 3000
ENV RAILS_ENV=development

CMD ["rails", "server", "-b", "0.0.0.0"]

EXPOSE $PORT
