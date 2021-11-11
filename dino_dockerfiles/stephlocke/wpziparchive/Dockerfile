FROM wordpress:php7.1-apache

# Add PHP Zip Archive extension
RUN apt-get install -y zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
&& docker-php-ext-install zip

# Install WP CLI
RUN curl -sSL -o /usr/local/bin/wp "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar" \
    && chmod +x /usr/local/bin/wp \
    && mkdir -p /etc/wp-cli \
    && chown www-data:www-data /etc/wp-cli

RUN echo "export WP_CLI_CONFIG_PATH=/etc/wp-cli/config.yml" > /etc/profile.d/wp-cli.sh

COPY docker-entrypoint.sh /entrypoint.sh

