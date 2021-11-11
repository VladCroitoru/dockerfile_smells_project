FROM ruby:2.3.1

# Install dependencies:
# - build-essential: To ensure certain gems can be compiled
# - nodejs: Compile assets
# - npm: Install node modules
# - yarn: Install & manage node modules [should make npm obsolete]
# - libpq-dev: Communicate with postgres through the postgres gem
# - postgresql-client-9.4: In case you want to talk directly to postgres
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install -qq -y build-essential nodejs yarn \
  libpq-dev postgresql-client-9.4 --fix-missing --no-install-recommends && \
  rm -rf /var/lib/apt/lists/*