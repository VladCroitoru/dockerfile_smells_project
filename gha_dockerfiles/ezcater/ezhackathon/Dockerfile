FROM ezcater-production.jfrog.io/ruby:2.7-pg13

ARG SKIP_REQUIRED_ENV_VAR_ENFORCEMENT=true
COPY Gemfile Gemfile.lock /usr/src/app/
ARG BUNDLE_EZCATER__JFROG__IO
RUN bundle install --without test development staging
ADD . /usr/src/app
RUN RAILS_ENV=production SECRET_KEY_BASE=fakekeybase bundle exec rails assets:precompile
EXPOSE 28076
CMD ["rails", "server", "-p", "28076", "-b", "0.0.0.0"]
