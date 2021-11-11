FROM jccwebservicesregistry.azurecr.io/source/drupal-nginx-fpm:1.2

ENV WEBSITES_CONTAINER_START_TIME_LIMIT "1800"
ENV WEBSITES_ENABLE_APP_SERVICE_STORAGE "true"

RUN rm -rf ${DRUPAL_BUILD}
RUN mkdir -p ${DRUPAL_BUILD}
COPY ./. ${DRUPAL_BUILD}/

WORKDIR ${DRUPAL_BUILD}
RUN composer install
RUN scripts/theme.sh -a
