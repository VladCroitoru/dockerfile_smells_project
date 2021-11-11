FROM ruby:2.4.5
LABEL maintainer="fenne035@umn.edu"

# Stolen from https://github.com/jfroom/docker-compose-rails-selenium-example

# Ugh, Yarn needs a newer version of Node
# See: https://github.com/yarnpkg/yarn/issues/6914#issuecomment-454165516
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash \
  && apt-get update && apt-get install -qq -y --no-install-recommends \
  build-essential nodejs \
  # Rails 5.1 expects Yarn to be a thing \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get install apt-transport-https -y \
  && apt-get update && apt-get install -y yarn

# For Capybara
RUN apt-get install -y -qq libqt4-dev libqtwebkit-dev

RUN mkdir -p /app
WORKDIR /app
COPY . .
# Add app files into docker image

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
RUN gem update --system ; gem install bundler:1.17.3; bundle config build.nokogiri --use-system-libraries
RUN bundle check || bundle install --without production

