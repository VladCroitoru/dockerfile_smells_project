ARG FROM=php:alpine
FROM $FROM
MAINTAINER Matthias Vogel <git@kanti.de>

# add file for https://github.com/pluswerk/grumphp-bom-task
# @see FROM https://github.com/alpine-docker/git
RUN apk --update add file bash rsync git openssh libxml2-dev patch imagemagick libpng-dev unzip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

# install ext-soap ext-mysqli ext-pcov
COPY --from=mlocati/php-extension-installer /usr/bin/install-php-extensions /usr/bin/
RUN install-php-extensions pcov soap mysqli gd zip @fix_letsencrypt

# @see FROM https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md
RUN wget https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer -O - -q > installer && \
    cat installer | php -- --filename="composer" --install-dir="/bin" && \
    cat installer | php -- --filename="composer1" --1 --install-dir="/bin" && \
    rm installer && \
    composer1 global require hirak/prestissimo && \
    composer1 clear-cache
