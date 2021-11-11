FROM ubuntu

MAINTAINER Santiago Saavedra <santiagosaavedra@gmail.com>

ENV TRACKS_VERSION 2.3.0
ENV RAILS_ENV production

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
       build-essential \
       bundler \
       curl \
       libsqlite3-dev \
       ruby \
       ruby-dev \
       rubygems-integration \
       sqlite3 \
       unzip \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/www && cd /var/www \
  && curl -L https://github.com/TracksApp/tracks/archive/v${TRACKS_VERSION}.zip -o source.zip \
  && unzip source.zip \
  && rm source.zip \
  && mv tracks-${TRACKS_VERSION} tracks \
  && chown -R www-data:www-data tracks \
  && rm /var/www/tracks/Gemfile

COPY ./Gemfile /var/www/tracks/
COPY ./database.yml ./site.yml /var/www/tracks/config/

RUN chown -R www-data:www-data /var/www/tracks /var/lib/gems/2.3.0 /usr/local/bin

WORKDIR /var/www/tracks

USER www-data

VOLUME ["/var/www/tracks/db"]

# Setup Tracks
#######################
RUN bundle install

RUN sed -i -e 's/serve_static_assets = false/serve_static_assets = true/' config/environments/production.rb

RUN bundle exec rake db:migrate # Initialize database

RUN bundle exec rake assets:precompile

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]

