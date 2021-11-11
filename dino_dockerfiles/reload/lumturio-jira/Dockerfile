FROM composer:2.1.11 AS build-env

RUN echo "phar.readonly=false" > "$PHP_INI_DIR/conf.d/phar-not-readonly.ini" && \
    composer global require kherge/box --prefer-dist --update-no-dev

COPY . /opt/lumturio-jira/

WORKDIR /opt/lumturio-jira

RUN composer install --prefer-dist --no-dev && \
    /tmp/vendor/bin/box build -v --no-interaction

FROM php:7.4.25-alpine

COPY --from=build-env /opt/lumturio-jira/lumturio-jira.phar /opt/lumturio-jira/lumturio-jira.phar

RUN apk add --no-cache tini=0.19.0-r0

# hadolint ignore=DL4006,SC2016
RUN crontab -l | { cat; echo '*/10    *       *       *       *       eval $(printenv | grep -E "^(JIRA|LUMTURIO)_" | sed "s/^\(.*\)$/export \1/g"); /opt/lumturio-jira/lumturio-jira.phar --verbose'; } | crontab -

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/usr/sbin/crond", "-f"]
