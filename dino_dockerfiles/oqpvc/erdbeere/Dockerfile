FROM ruby:2.4.0

MAINTAINER oqpvq <o+docker@qp.vc>
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ENV RAILS_ENV=production

EXPOSE 3000
CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0", "-p", "3000"]

RUN apt-get update && apt-get install -y nodejs sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/oqpvc/erdbeere.git .
RUN bundle install
RUN bundle exec rake assets:precompile
RUN bundle exec rake db:schema:load
RUN bundle exec rake db:seed


