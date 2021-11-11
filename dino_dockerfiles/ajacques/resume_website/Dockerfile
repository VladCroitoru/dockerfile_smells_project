FROM ruby:3.0-buster AS prereq

RUN echo 'gem: --no-document' > /etc/gemrc

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install -qy libmariadb3 ruby-dev nodejs build-essential \
    libmariadb-dev libsqlite-dev libffi-dev yarn
RUN gem install bundler

WORKDIR /rails-app

FROM prereq AS npm

ADD package.json /rails-app
ADD yarn.lock /rails-app

RUN yarn install

FROM prereq AS prep

ADD Gemfile /rails-app
ADD Gemfile.lock /rails-app

RUN bundle config set without 'test development' \
  && bundle install

COPY --from=npm /rails-app/node_modules /rails-app/node_modules

ADD . /rails-app

# Generate compiled assets + manifests
RUN export RAILS_ENV=assets \
  && rake assets:precompile \
  && rm -rf test tmp/* log/* node_modules \
# All files/folders should be owned by root but readable by www-data
  && find . -type f -exec chmod 444 {} \; \
  && find . -type d -print -exec chmod 555 {} \; \
  && chown -R 9999:9999 tmp \
  && chmod 755 db \
  && find tmp -type d -print -exec chmod 755 {} \; \
  && find bin runit -type f -print -exec chmod 555 {} \; \
  && mkdir -m 755 runit/nginx/supervise runit/rails/supervise \
  && rails tmp:create

# Final Phase
RUN bundle config set without 'test development assets' \
  && bundle install \
  && bundle clean --force

RUN rm -rf /usr/local/bundle/cache

FROM ruby:3.0-slim-buster

RUN apt-get update \
  && apt-get install -qy --no-install-recommends runit nginx libxml2 libmariadb3 ca-certificates \
# Uninstall development headers/packages
  && apt-get clean autoclean \
  && apt-get autoremove --yes \
  && rm -rf /var/lib/{apt,dpkg,cache,log}/ \
  && rm -rf /var/cache/* /root \
  && adduser -u 9999 -H -h /rails-app -S www-data \
  && mkdir /var/lib/nginx/body \
  && chown www-data:www-data /var/lib/nginx /usr/share/nginx/

COPY --from=prep /usr/local/bundle /usr/local/bundle
COPY --from=prep /rails-app /rails-app
WORKDIR /rails-app

EXPOSE 8080 8081
CMD ["/usr/bin/runsvdir", "/rails-app/runit"]
