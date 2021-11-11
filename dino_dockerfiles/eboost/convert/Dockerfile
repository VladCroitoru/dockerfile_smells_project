FROM php:latest

MAINTAINER Bert van Hoekelen

#Install unoconv
RUN apt-get update && apt-get install -y unoconv imagemagick && apt-get clean

# Install fonts
RUN echo "deb http://mirror.transip.net/debian/debian jessie non-free contrib" >> /etc/apt/sources.list
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y unar fonts-liberation msttcorefonts && apt-get clean
RUN wget http://download.microsoft.com/download/E/6/7/E675FFFC-2A6D-4AB0-B3EB-27C9F8C8F696/PowerPointViewer.exe && \
    unar PowerPointViewer.exe && \
    rm PowerPointViewer.exe && \
    unar PowerPointViewer/ppviewer.cab && \
    mkdir ~/.fonts/ && \
    cp ppviewer/*.TTF ppviewer/*.TTC ~/.fonts/ && \
    rm -Rf PowerPointViewer

# Install php extensions
RUN apt-get install -y libicu-dev libmcrypt-dev git && docker-php-ext-install intl mcrypt mbstring

# Install imagick extension
RUN apt-get install libmagickwand-dev -y \
    && pecl install imagick \
    && docker-php-ext-enable imagick

RUN docker-php-ext-install zip

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer

# Copy app source
ADD [".", "/convert"]

# Change working directory
WORKDIR "/convert"

COPY max_upload.ini /usr/local/etc/php/conf.d/max_upload.ini

# Install dependencies with Composer.
# --prefer-source fixes issues with download limits on Github.
# --no-interaction makes sure composer can run fully automated
RUN composer install --prefer-source --no-interaction

EXPOSE 3000

CMD ["php", "-S", "0.0.0.0:3000", "server.php"]