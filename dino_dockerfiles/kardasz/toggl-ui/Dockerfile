FROM webinventions/php7-fpm-nginx:newrelic

# Maintainer
LABEL maintainer "krzysztof@kardasz.eu"

# add configs & data after package install (so packages won't override them)
ADD ./docker-files/etc /etc
ADD ./docker-files/usr /usr

WORKDIR /var/www

# Sources
RUN rm -rf /var/www/*
ADD ./ /var/www

# Composer
RUN \
    composer -n --no-ansi --no-scripts install && \
    composer dump-autoload --optimize