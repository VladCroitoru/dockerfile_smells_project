FROM ruby:3.0.2
LABEL maintainer="kent@slaymakercellars.com"

ARG USERNAME
ARG UID
ARG GID

RUN echo "$USERNAME:1234:$UID:$GID:docker-user,,,:/app/:/bin/bash" >> /etc/passwd

RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && \
  apt-get install -y \
  build-essential \
  yarn \
  nodejs \
  postgresql-client

ENV BUNDLE_PATH /gems
ENV PATH $BUNDLE_PATH/bin:$GEM_HOME/gems/bin:$PATH

WORKDIR /app
EXPOSE 3000

RUN echo " \
  alias rspec='RAILS_ENV=test bundle exec rspec' \n\
  alias rails='bundle exec rails' \n\
  alias rake='bundle exec rake'  \n\
  alias rubocop='bundle exec rubocop'  \n\
  alias ls='ls --color=auto' \n\
  " >> ~/.bashrc


RUN gem install bundler

ENTRYPOINT [ "./script/docker-entrypoint.sh" ]
