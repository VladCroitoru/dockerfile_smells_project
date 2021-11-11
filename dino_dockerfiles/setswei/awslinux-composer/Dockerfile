# Select Source Docker/OS
FROM amazonlinux:latest

# Author
MAINTAINER setswei <kyle.hartigan@cybercrysis.net.au>

# PHP70 Packages
RUN yum install -y php70 \
    php70-cli \
    php70-gd \
    php70-ldap \
    php70-mbstring \
    php70-mcrypt \
    php70-mysqlnd \
    php70-pdo \
    php70-pecl-apc \
    php70-pecl-imagick \
    php70-soap \
    php70-intl \
    php7-pear \
    gcc

# Clean up YUM when completed
RUN yum clean all

# Add Composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer

# Composer Version
RUN composer --version