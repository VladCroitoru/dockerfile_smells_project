FROM nonfiction/wordpress-base:v1

# Copy the codebase
COPY ./app /srv/app
COPY ./config /srv/config
COPY ./src /srv/src
COPY ./theme /srv/theme
COPY ./vendor /srv/vendor
COPY ./web /srv/web
RUN ln -sf /srv/theme /srv/web/content/themes/theme
COPY ./composer.json /srv/composer.json

# Persist uploads in this volume
VOLUME /srv/web/content/uploads

# Give Apache permissions for /content dir
RUN chown -R www-data:www-data /srv/web/content

# This script starts Apache Server
COPY ./run.sh /srv/run.sh
RUN chmod +x /srv/run.sh
CMD ["/srv/run.sh"]
