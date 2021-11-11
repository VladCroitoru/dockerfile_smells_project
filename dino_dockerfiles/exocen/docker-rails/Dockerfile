FROM exocen/docker-ruby:latest
MAINTAINER Exo

RUN apt-get update

#Install imageMagic
RUN apt-get install -qq -y imagemagick

#Install Vim
RUN apt-get install -qq -y vim

# Install nodejs
RUN apt-get install -qq -y nodejs

# Intall software-properties-common for add-apt-repository
RUN apt-get install -qq -y software-properties-common

# Install Nginx.
RUN add-apt-repository -y ppa:nginx/development
RUN apt-get update -qq
RUN apt-get install -qq -y nginx-extras
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
RUN chown -R www-data:www-data /var/lib/nginx
# Add default nginx config
ADD nginx-sites.conf /etc/nginx/sites-enabled/default
ADD nginx_https.conf /etc/nginx/default_https

# Install foreman
RUN gem install foreman

# Install the latest postgresql lib for pg gem
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --force-yes libpq-dev

# Install MySQL(for mysql, mysql2 gem)
RUN apt-get install -qq -y libmysqlclient-dev


# Generate certificat
WORKDIR  /etc/ssl/certs
RUN openssl dhparam -dsaparam -out dhparam.pem 4096

# Install Rails App
WORKDIR /app
ONBUILD ADD Gemfile /app/Gemfile
ONBUILD ADD Gemfile.lock /app/Gemfile.lock
ONBUILD RUN bundle install --without development test
ONBUILD ADD . /app

# Add letsEncrypt
RUN wget https://dl.eff.org/certbot-auto

# Add default unicorn config
ADD unicorn.rb /app/config/unicorn.rb

# Add default foreman config
ADD Procfile /app/Procfile

ENV RAILS_ENV production

CMD bundle exec rake assets:precompile && foreman start -f Procfile
