FROM wdst-ocp-drupal-base:1.0
COPY --chown=1001:1 src /code
USER 1001
RUN chmod -R g+rwX /code
RUN cd /code && rm -rf .git && composer install && composer update
