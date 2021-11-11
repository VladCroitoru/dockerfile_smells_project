# Use an official PHP runtime as a base image
FROM hexaua/dev

# ADD copyright
LABEL maintainer = "a.ohanov@hexa.com.ua"

# Install any needed packages
RUN pecl install xdebug-2.5.0 \
    && docker-php-ext-enable xdebug \
    && docker-php-ext-install sockets

RUN apt-get update -y

RUN apt-get install -y default-jre \
    curl \
    net-tools \
    xvfb \
    iceweasel \
    mysql-client \
    libmysqlclient-dev -yqq --no-install-recommends

RUN apt-get purge -y g++ \
    && apt-get autoremove -y \
    && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer


RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs build-essential
RUN npm install -g bower

# Dubug info
RUN node -v
RUN npm -v