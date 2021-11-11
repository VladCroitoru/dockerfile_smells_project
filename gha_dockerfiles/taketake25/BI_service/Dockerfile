# syntax=docker/dockerfile:1
FROM ruby:2.7.0
RUN apt-get update -qq && apt-get install -y default-mysql-client

# install nodejs >= 12
RUN curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs
RUN node -v

RUN apt-get update && apt-get install -y curl apt-transport-https wget && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -y yarn

WORKDIR /app
COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN bundle install
COPY . /app

RUN yarn add -D hard-source-webpack-plugin
RUN rails tailwindcss:install

# Add a script to be executed every time the container starts.
COPY entrypoint.sh /usr/bin/
COPY wait-for-it.sh /usr/bin/

RUN chmod +x /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/wait-for-it.sh
# ENTRYPOINT ["wait-for-it.sh", "db:3306", "-t", "0", "--", "entrypoint.sh"]
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 3000

# Configure the main process to run when running the image
CMD ["rails", "server", "-b", "0.0.0.0"]


