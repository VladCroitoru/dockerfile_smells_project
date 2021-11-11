FROM ubuntu:16.04

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y htop curl nano


# Install PHP
RUN apt-get install -y php7.0 php7.0-mbstring php7.0-dom

# Install Laravel + Composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv /composer.phar /usr/bin/composer

# Additional dependeces
RUN apt-get install -y git
RUN apt-get install -y zip unzip
RUN apt-get install -y php7.0-zip

# Create user
RUN groupadd -r -g 1000 laravel && \
    useradd -mr -c "Laravel" -d "/app" -g 1000 -u 1000 laravel

# App dir
USER laravel
RUN mkdir -p /app
WORKDIR /app

ENV PATH="/app/.composer/vendor/bin:${PATH}"
