FROM composer:2 AS composer

FROM php:8.0-alpine

COPY --from=composer /usr/bin/composer /usr/bin/composer

LABEL "com.github.actions.name"="nucleos/auto-merge-action"
LABEL "com.github.actions.description"="Automerge labeled GitHub Pull Requests."
LABEL "com.github.actions.icon"="git-merge"
LABEL "com.github.actions.color"="green"

LABEL "repository"="http://github.com/nucleos/auto-merge-action"
LABEL "homepage"="http://github.com/nucleos/auto-merge-action"
LABEL "maintainer"="Christian Gripp <mail@core23.de>"

WORKDIR /app

ADD . /app/

RUN COMPOSER_CACHE_DIR=/dev/null composer install --no-dev --no-scripts

ENTRYPOINT ["/app/entrypoint.sh"]
