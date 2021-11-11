FROM ruby:1.9

# ruby:1.9 is based on Debian Jessie, which has been archived now
# we also need jessie-backports to support the new Let's Encrypt Root CA
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list

# jessie-backports repo expired, so we need to avoid checking the date (see https://unix.stackexchange.com/a/508728/49371 )
RUN printf 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf

# Cleanup expired Let's Encrypt CA (Sept 30, 2021)
RUN sed -i '/^mozilla\/DST_Root_CA_X3/s/^/!/' /etc/ca-certificates.conf && update-ca-certificates -f

# Install nodejs (ignoring GPG's signature expiration, since Debian Jessie won't get those updated: https://wiki.debian.org/DebianJessie )
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes nodejs && \
  # I wasn't able to pin-point which packages need to be updated in order for Let's Encrypt new Root CA to work
  # Upgrading every available package does the trick - so we'll go with that, even at the cost of a larger Docker image
  DEBIAN_FRONTEND=noninteractive apt-get upgrade -y --force-yes && \
  apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update gem version to one that's compatible with Let's Encrypt new Root CA
RUN gem update --system 1.8.30

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app
RUN bundle install --jobs 3 --deployment --without development test

# Install the application
ADD . /app

# Link Twitter config file
RUN ln -s /run/secrets/twitter_oauth_consumer.yml /app/config

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production

# Add config files
ADD docker/database.yml /app/config/database.yml
ADD docker/amqp.yml /app/config/amqp.yml
ADD docker/migrate /app/migrate

ENV RAILS_LOG_TO_STDOUT=true
ENV RAILS_ENV=production
ENV WEB_BIND_URI=tcp://0.0.0.0:80
ENV PUMA_TAG=nuntium
ENV WEB_PUMA_FLAGS=
EXPOSE 80

CMD exec puma -e $RAILS_ENV -b $WEB_BIND_URI --tag $PUMA_TAG $WEB_PUMA_FLAGS
