FROM ubuntu:19.04

ADD . /rails-app
WORKDIR /rails-app
RUN export BUILD_PKGS="gnupg libsqlite3-dev zlib1g-dev libghc-zlib-dev libpq-dev ruby-dev g++ make patch nodejs curl" \
  && apt-get update \
  && apt-get install --no-install-recommends -qy ruby libsqlite3-0 libpq5 $BUILD_PKGS \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
  && apt-get update \
  && apt-get install --no-install-recommends -qy yarn \
  && gem install bundler --no-ri --no-rdoc \
  && env bundle install --without test development \
  && yarn install --frozen-lockfile --prod --no-interactive --silent \
# Generate compiled assets + manifests
  && NODE_ENV=production RAILS_ENV=assets rake release \
# Remove the source assets because we don't need them anymore
  && rm -rf app/assets/* app/javascript/* node_modules yarn.lock \
# Uninstall development headers/packages
  && apt-get -qy purge $BUILD_PKGS yarn \
  && apt-get -qy autoremove \
  && rm -rf /var/lib/gems/2.3.0/cache /var/cache/* /root /var/lib/apt/info/* /var/lib/apt/lists/* /var/lib/ghc \
     ./tmp/* ./bundle /usr/local/share/.cache/yarn /var/lib/dpkg /var/lib/log/*  \
# All files/folders should be owned by root by readable by www-data
  && find . -type f -print -exec chmod 444 {} \; \
  && find . -type d -print -exec chmod 555 {} \; \
  && chown -R www-data:www-data tmp \
  && chmod 755 db && find tmp -type d -print -exec chmod 755 {} \; \
  && find bin -type f -print -exec chmod 544 {} \;
ENV RAILS_ENV=production
USER www-data
EXPOSE 8080
ENTRYPOINT ["/usr/bin/ruby", "/rails-app/bin/bundle", "exec"]
CMD ["/usr/local/bin/unicorn", "-o", "0.0.0.0", "-p", "8080", "-c", "unicorn.rb", "--no-default-middleware"]
