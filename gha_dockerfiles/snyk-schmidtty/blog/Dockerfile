FROM ruby:2.5.1

RUN apt-get update &&\
    apt-get install -y git vim sqlite3 &&\
    rm -rf /var/lib/apt/lists/*

RUN gem update --system 3.0.4 &&\
    gem install bundler -v '2.0.2'

WORKDIR /blog

COPY --from=purpledobie/blog:gems-bad /blog .

ENV BUNDLER_VERSION 2.0.2
ENV RAILS_ENV=development
RUN bundle config --local path vendor/bundle && bundle config --local without assets &&\
    bundle exec rails db:setup &&\
    bundle exec rails db:migrate

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"] 
