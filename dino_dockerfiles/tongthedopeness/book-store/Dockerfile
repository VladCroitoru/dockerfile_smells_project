FROM tongthedopeness/alpine-ruby

WORKDIR /usr/src/app

COPY Gemfile Gemfile.lock ./
RUN bundle install --without test development && bundle clean

COPY . /usr/src/app

RUN RAILS_ENV=production bundle exec rake assets:precompile

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]