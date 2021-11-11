# Drupal development container

FROM karelbemelmans/d7-docker-base:1.0
MAINTAINER Karel Bemelmans <mail@karelbemelmans.com>

# Additinal Drupal settings can be put in the extra.settings.php file.
# If this file exists it will be included at the bottom of settings.php
COPY config/extra.settings.php sites/default/extra.settings.php

# Drupal Libraries
#
# Colorbox, needed for the colorbox contrib module
RUN curl -L --silent https://github.com/jackmoore/colorbox/archive/1.x.zip -o /tmp/colorbox.zip \
      && unzip /tmp/colorbox.zip -d sites/all/libraries/ \
      && mv sites/all/libraries/colorbox-1.x sites/all/libraries/colorbox \
      && rm -f /tmp/colorbox.zip

# Drupal Modules
RUN drush dl colorbox zen

# Drupal public files
RUN mkdir -p sites/default/files && chown www-data:www-data sites/default/files
VOLUME /var/www/html/sites/default/files

# Drupal private files. You should enter this path in your configuration.
RUN mkdir -p /data/private && chown www-data:www-data /data/private
VOLUME /data/private

# Done.
