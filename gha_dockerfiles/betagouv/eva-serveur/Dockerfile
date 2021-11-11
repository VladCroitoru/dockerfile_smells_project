FROM ruby:2.6

ARG RAILS_ENV
ENV RAILS_ENV ${RAILS_ENV}

WORKDIR /app/

COPY Gemfile Gemfile.lock ./
RUN bundle install --without development test --deployment --jobs 4 --retry 3 --quiet

COPY . ./

RUN bundle exec rails assets:precompile RAILS_ENV=${RAILS_ENV} SECRET_KEY_BASE=ceci-est-une-fausse-secret-key-pour-que-rails-accepte-de-demarrer

EXPOSE 3000

CMD bash -c "rm -f tmp/pids/server.pid && bundle exec rails server"
