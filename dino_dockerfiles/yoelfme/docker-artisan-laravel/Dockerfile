FROM dylanlindgren/docker-laravel-artisan

MAINTAINER "Yoel Monzon" <yoelfme@hotmail.com>

RUN apt-get update && apt-get install -y php5-curl

RUN apt-get update -y && \
    apt-get install -y \
    make \
    php5-dev \
    php-pear \
    imagemagick \
    libmagickwand-dev \
    libmagickcore-dev

RUN pecl install imagick --with-apxs='/usr/bin/apxs2'

RUN apt-get install -y \
    php5-imagick

CMD ["--help"]