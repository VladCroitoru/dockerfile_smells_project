# Docker container image for Entersection WordPress instance
# https://github.com/bitnami/bitnami-docker-wordpress
FROM bitnami/wordpress:latest
MAINTAINER gregoryfoster <greg@foojutsu.com>

ENV WORDPRESS_DB_NAME=wp_entersection \
    WORDPRESS_DB_USER=wp_admin \
    WORDPRESS_DB_PASSWORD=123456 \
    WP_CLI_VERSION='1.0.0'

# Install cURL
RUN apt-get update \
 && apt-get -y install curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Download and install WordPress CLI
RUN curl -L "https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar" > /usr/bin/wp \
 && chmod +x /usr/bin/wp

# Copy post-installation script
COPY entersection-configure_wordpress.sh /entersection-configure_wordpress.sh
