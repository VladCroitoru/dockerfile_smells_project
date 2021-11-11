FROM        php:7.4-apache

######################################
# Install and configure dependencies #
######################################

RUN         apt-get update \
            && apt-get upgrade -y \
            && apt-get install -y \
                bzip2 \
                curl \
                fontconfig \
                g++ \
                git \
                gnupg \
                libonig-dev \
                libfreetype6 \
                libicu-dev \
                libjpeg-dev \
                libpcre3-dev \
                libpng-dev \
                libzip-dev \
                mariadb-client \
                postgresql-9.5 \
                postgresql-server-dev-all \
                rsync \
                unzip \
                zip \
            && rm -rf /var/lib/apt/lists/* \
            && docker-php-ext-install exif \
            && docker-php-ext-configure gd --with-jpeg \
            && docker-php-ext-install gd \
            && docker-php-ext-install intl \
            && docker-php-ext-install mbstring \
            && docker-php-ext-install mysqli \
            && docker-php-ext-install pdo_mysql \
            && docker-php-ext-install pdo_pgsql \
            && docker-php-ext-configure zip \
            && docker-php-ext-install zip \
            && a2enmod rewrite \


####################
# Install Composer #
####################

            && curl -sS https://getcomposer.org/installer | php \
            && mv composer.phar /usr/local/bin/composer \

###############
# Install NPM #
###############

            && curl -sL https://deb.nodesource.com/setup_10.x | bash - \
            && apt install -y nodejs \

#######################
# Install Grunt, Gulp #
#######################

            && npm install -g \
                bower \
                grunt-cli \
                gulp-cli

####################
# Add config files #
####################

COPY        ./php/php.ini /usr/local/etc/php/php.ini
COPY        ./apache/000-default.conf /etc/apache2/sites-available/000-default.conf
COPY        ./scripts/init-container.sh /root/init-container.sh

###############################
# Configure working directory #
###############################

WORKDIR     /www

################
# Expose ports #
################

EXPOSE      80

#########################
# Configure stop signal #
#########################

STOPSIGNAL  SIGTERM

#######
# Run #
#######

CMD         bash /root/init-container.sh /www \
            && apache2-foreground
