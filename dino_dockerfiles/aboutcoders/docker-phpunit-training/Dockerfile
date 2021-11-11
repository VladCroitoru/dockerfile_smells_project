# PHP 7.1.6 and Apache based on official PHP image.
# Adding Xdebug, PHPUnit 6.2 and dependencies in order to provide
# a sandbox for testing PHPUnit with training purposes.

FROM php:7.1.6-apache

# Preset PHP.ini values.
COPY config/php.ini /usr/local/etc/php/

# Adding dependencies and tools
RUN apt-get update && apt-get install -y \
        apt-utils \
        sudo \
        vim \
        git \
        zip \
        wget \
        tree \
        zsh

# Adding Xdebug
RUN pecl install xdebug-2.5.5 \
    && docker-php-ext-enable xdebug

# Adding Composer
WORKDIR /tmp
RUN curl --silent --show-error https://getcomposer.org/installer | php
RUN ["/bin/bash", "-c", "mv /tmp/composer.phar /usr/bin/composer"]

# Add user to not use root during testing
RUN useradd --create-home --no-log-init --shell /bin/bash tester \
    && echo 'tester:testerpwd' | chpasswd \
    && adduser tester sudo

# Default directory entry for the image:
WORKDIR /home/tester

# Add PHPUnit and recommended dependencies
RUN su tester -c "composer require 'phpunit/phpunit:~6.2' --prefer-source --no-interaction" \
    && su tester -c "composer require 'phpunit/dbunit' --prefer-source --no-interaction"

# Default user for container interaction
USER tester

# Create a phpunit example for testing:
COPY examples /home/tester/examples

# Adding oh-my-zsh
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

# Adding specific theme for oh-my-zsh in order to clarify commands during training:
COPY config/oh-my-zsh/bullet-train.zsh-theme /home/tester/.oh-my-zsh/custom/themes/bullet-train.zsh-theme
COPY config/oh-my-zsh/.zshrc /home/tester/.zshrc

# Expose port 80 for apache to the host machine
EXPOSE 80

# Mount apache web folder for testing
VOLUME /var/www/html

# Overwrite the entry point (it's apache logs by default in parent image)
ENTRYPOINT ["/bin/zsh"]
