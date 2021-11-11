FROM infoslack/docker-ruby

MAINTAINER Daniel Romero <infoslack@gmail.com>

RUN apt-get update \
        && apt-get install -y \
            nodejs \
            mysql-client \
            postgresql-client \
            sqlite3 \
            --no-install-recommends
        && rm -rf /var/lib/apt/lists/*

ENV RAILS_VERSION 4.2.0

RUN gem install rails --version "$RAILS_VERSION"
