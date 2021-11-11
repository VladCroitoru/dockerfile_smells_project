FROM ruby:2.3 as build

# Cleanup expired Let's Encrypt CA (Sept 30, 2021)
RUN sed -i '/^mozilla\/DST_Root_CA_X3/s/^/!/' /etc/ca-certificates.conf && update-ca-certificates -f

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app

RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install gems
RUN bundle install --jobs 10 --without development test

# Install the application
ADD . /app

# Precompile assets
RUN bundle exec rake assets:precompile RAILS_ENV=production SECRET_KEY_BASE=secret

FROM ruby:2.3

# Cleanup expired Let's Encrypt CA (Sept 30, 2021)
RUN sed -i '/^mozilla\/DST_Root_CA_X3/s/^/!/' /etc/ca-certificates.conf && update-ca-certificates -f

# Install gem bundle
ADD Gemfile /app/
ADD Gemfile.lock /app/
WORKDIR /app

# Install the application
ADD . /app

# Install extra files
ADD docker/migrate       /app/migrate
ADD docker/database.yml  /app/config/database.yml

# Copy bundle and assets
COPY --from=build /usr/local/bundle /usr/local/bundle
COPY --from=build /app/public/assets /app/public/assets

ENV RAILS_LOG_TO_STDOUT=true
ENV RAILS_ENV=production
ENV BIND=tcp://0.0.0.0:80
ENV PUMA_TAG=guisso
ENV PUMA_PARAMS=
EXPOSE 80

CMD exec puma -e $RAILS_ENV -b $BIND --tag $PUMA_TAG $PUMA_PARAMS
