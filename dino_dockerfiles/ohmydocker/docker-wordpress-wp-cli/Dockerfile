#
# Installs WordPress with wp-cli (wp.cli.org) installed
# Docker Hub: https://registry.hub.docker.com/u/conetix/wordpress-with-wp-cli/
# Github Repo: https://github.com/conetix/docker-wordpress-wp-cli

FROM wordpress:latest

# OhMyDocker Version
ENV OMDWP 1.0.5

ENV WORDPRESS_DB_USER="" \
  WORDPRESS_DB_PASSWORD="" \
  WORDPRESS_DB_NAME="" \
  WORDPRESS_DB_HOST="" \
  WORDPRESS_SITE_URL="" \
  WORDPRESS_PORT="" \
  WORDPRESS_ADMIN_EMAIL="" \
  WORDPRESS_ADMIN_USER="" \
  WORDPRESS_ADMIN_PASSWORD="" \
  WORDPRESS_TITLE="" \
  WORDPRESS_TAGLINE=""

# Configure SU script for www-data as /bin/wp
COPY wp-su.sh /bin/wp

# Bring in the assets
COPY assets /assets

# Install Linux Apps and WP-CLI PHP Archive / Cleanup / Perms
RUN apt-get update && apt-get install -y sudo less; \
  curl -o /bin/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar; \
  chmod +x /bin/wp-cli.phar /bin/wp; \
  apt-get clean; \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \
  chmod +x /assets/*.sh
