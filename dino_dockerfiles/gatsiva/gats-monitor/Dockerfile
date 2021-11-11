# ########################################################################################
# GATS COMMAND LINE MONITOR
#
# This is a stand-alone container utilizing PHP 7 designed to be able to monitor conditions
# and email indicators, utilizing the CEE. It is driven from a config.json file that needs
# to be located in /etc/gats-monitor.
#
# For detailed documentation, please see the README.md file
#

FROM php:7.1-cli-alpine

MAINTAINER Christopher Scheidel <cscheide@oiltycoonsllc.com>

# Update and install system dependencies
RUN apk add --no-cache curl

# Install composer
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer

# Install the code
RUN mkdir -p /usr/src/app && mkdir -p /etc/gats-monitor
COPY src/* /usr/src/app/
WORKDIR /usr/src/app

# Install vendor files
RUN cd /usr/src/app && composer install

# Run the app when launched
ENTRYPOINT ["php","./app.php"]

# Using the default config location
CMD ["/var/gatsiva/cli-config.json"]
