#
# Installs WordPress with wp-cli (wp.cli.org) installed
# Docker Hub: https://registry.hub.docker.com/u/conetix/wordpress-with-wp-cli/
# Github Repo: https://github.com/conetix/docker-wordpress-wp-cli

FROM wordpress:latest

ENV WORDPRESS_DB_USER="" \
  WORDPRESS_DB_PASSWORD="" \
  WORDPRESS_DB_NAME="" \
  WORDPRESS_DB_HOST="" \
  WORDPRESS_SITE_URL=""

# Configure SU script for www-data as /bin/wp
COPY wp-su.sh /bin/wp

# Install Linux Apps (+mysql client for wp-cli) and WP-CLI PHP Archive / Cleanup / Perms
RUN apt-get update && apt-get install -y sudo less mysql-client; \
  curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar; \
  chmod +x /bin/wp-cli.phar /bin/wp; \
  apt-get clean; \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;

VOLUME /var/www/html /assets