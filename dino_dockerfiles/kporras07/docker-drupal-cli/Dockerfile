FROM ubuntu:16.04

MAINTAINER Kevin Porras <kporras07@gmail.com>

RUN apt-get clean -y && apt-get update -y && apt-get install -y locales

# Set timezone aand locale.
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Prevent services autoload (http://jpetazzo.github.io/2013/10/06/policy-rc-d-do-not-start-services-automatically/)
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d

RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install python-software-properties software-properties-common

# Adding https://launchpad.net/~ondrej/+archive/ubuntu/php PPA repo for php.
RUN add-apt-repository ppa:ondrej/php

# Basic packages
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install \
    supervisor \
    curl \
    wget \
    zip \
    unzip \
    git \
    mysql-client \
    pv \
    apt-transport-https \
    vim \
    patch \
    --no-install-recommends && \
    # Cleanup
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# PHP packages
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install \
    php7.3-common \
    php7.3-cli \
    php-pear \
    php7.3-mbstring \
    php7.3-mysql \
    php7.3-curl \
    php7.3-gd \
    php7.3-sqlite \
    php7.3-json \
    php7.3-memcache \
    php7.3-intl \
    php-xdebug \
    php7.3-xml \
    php7.3-bcmath \
    --no-install-recommends && \
    # Cleanup
    DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install nvm and a default node version
ENV NVM_VERSION 0.33.4
ENV NODE_VERSION 6.10.1
ENV NVM_DIR $HOME/.nvm
RUN \
    curl -sSL https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh | bash && \
    . $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && \
    nvm alias default $NODE_VERSION && \
    # Install global node packages
    npm install -g npm && \
    npm install -g grunt-cli && \
    npm install -g gulp-cli
ENV PATH /.npm/versions/node/$NODE_VERSION/bin:$PATH

# Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Drush and Drupal Coder.
RUN composer global require drupal/coder
RUN wget -O /tmp/drush.phar https://github.com/drush-ops/drush-launcher/releases/download/0.6.0/drush.phar
RUN chmod +x /tmp/drush.phar
RUN mv /tmp/drush.phar /usr/local/bin/drush

# Install Robo
RUN wget https://robo.li/robo.phar
RUN chmod +x robo.phar && mv robo.phar /usr/local/bin/robo

# Install ahoy
RUN wget -q https://github.com/ahoy-cli/ahoy/releases/download/2.0.0/ahoy-bin-linux-amd64 -O /usr/local/bin/ahoy && chmod +x /usr/local/bin/ahoy

# PHP settings changes
RUN sed -i 's/memory_limit = .*/memory_limit = 512M/' /etc/php/7.3/cli/php.ini && \
    sed -i 's/max_execution_time = .*/max_execution_time = 300/' /etc/php/7.3/cli/php.ini

WORKDIR /var/www/html

# Add Composer bin directory to PATH
ENV PATH /root/.composer/vendor/bin:$PATH

# SSH settigns
COPY config/.ssh /root/.ssh

# Startup script
COPY ./startup.sh /opt/startup.sh
RUN chmod +x /opt/startup.sh

# Starter script
ENTRYPOINT ["/opt/startup.sh"]

# By default, launch supervisord to keep the container running.
CMD /usr/bin/supervisord -n
