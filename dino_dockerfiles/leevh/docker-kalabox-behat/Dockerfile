FROM drush/drush:8-php5

# Add files and folders to container.
ADD ["composer.json", "entrypoint.sh", "/srv/"]
WORKDIR /srv

# Install and initialize Behat, create folder for artifacts.
RUN composer install \
    && bin/behat --init

ENTRYPOINT ["/srv/entrypoint.sh"]
