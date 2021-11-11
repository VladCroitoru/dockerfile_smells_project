FROM php:7-fpm

RUN apt-get update && apt-get install -y \
  git \
  nginx-light \
  unzip \
  zip 

# Install composer
RUN curl -sS https://getcomposer.org/installer \
  | php -- --install-dir=/usr/local/bin --filename=composer 

# Install tini (init wrapper) for nicer signal trapping
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

WORKDIR /var/www

# Faster builds when composer.json doesn't change
COPY composer.json /var/www/
RUN composer install --no-dev

COPY . /var/www

COPY ./docker/nginx/vhost.conf /etc/nginx/sites-available/default
COPY ./docker/startup /startup 

CMD ["/startup"]
