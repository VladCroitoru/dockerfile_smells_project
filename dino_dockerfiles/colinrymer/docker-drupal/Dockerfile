FROM centurylink/apache-php:latest
MAINTAINER CenturyLink

# Install packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \
  apt-get -y install mysql-client && \
  apt-get -y install postgresql-client

# Install Drush
RUN pear channel-discover pear.drush.org && pear install drush/drush

# Download latest stable Drupal into /app
RUN rm -fr /app && drush dl drupal --drupal-project-rename=app

# Apply opcode cache patch (see https://www.drupal.org/node/779482)
RUN cd app && curl https://www.drupal.org/files/issues/779482-clear-opcode-cache-129.patch | git apply -

#Config and set permissions for setting.php
RUN cp app/sites/default/default.settings.php app/sites/default/settings.php && \
    chmod a+w app/sites/default/settings.php && \
    chmod a+w app/sites/default

EXPOSE 80

CMD exec supervisord -n
