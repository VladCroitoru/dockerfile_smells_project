FROM nextcloud:12.0.0-apache

COPY docker.config.php autoconfig.php /usr/src/nextcloud/config/
RUN chown --recursive www-data:www-data /usr/src/nextcloud/config

ENV NEXTCLOUD_DATA_PATH="/var/opt/nextcloud"
RUN mkdir -p "${NEXTCLOUD_DATA_PATH}" && \
    touch "${NEXTCLOUD_DATA_PATH}/.ocdata" && \
    chown --recursive www-data:www-data "${NEXTCLOUD_DATA_PATH}"
