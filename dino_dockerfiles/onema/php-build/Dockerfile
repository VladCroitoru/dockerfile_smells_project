FROM php:7.3-apache

# Install python and pip
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python && \
    apt-get -y install python-pip && \
    pip install boto3

# Install php extensions
RUN apt-get -y install zlib1g-dev &&  \
    apt-get -y install libzip-dev && \
    docker-php-ext-install zip pdo pdo_mysql

# Install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('sha384', 'composer-setup.php') === '106d3d32cc30011325228b9272424c1941ad75207cb5244bee161e5f9906b0edf07ab2a733e8a1c945173eb9b1966197') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    mv composer.phar /usr/local/bin/composer

# Install nodejs
RUN apt-get update && apt-get install -my wget gnupg && \
    curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh && \
    chmod +x nodesource_setup.sh && \
    ./nodesource_setup.sh && \
    apt-get install nodejs && \
    rm nodesource_setup.sh

WORKDIR /var/www/html/
