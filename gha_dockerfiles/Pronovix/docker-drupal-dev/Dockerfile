ARG PHP_IMAGE="wodby/drupal-php:7.3-dev"

FROM ${PHP_IMAGE}

ARG COMPOSER_VERSION

USER root

RUN set -xe; \
  # Composer version is locked because certain versions have worse performance than others.
  # Currently the known good versions: 1.7.3, 1.10.5, 1.10.15, 1.10.17
  # TODO Drop Composer 1 support in 2021 Q1.
  # The default 1x version is hardcoded to a "good one" but if a specific version is passed then it is respected, like
  # '1.10.5'.
  if [[ "${COMPOSER_VERSION}" -eq 1 ]]; then COMPOSER_VERSION="-- 1.10.17"; else if [[ "${COMPOSER_VERSION}" -eq 2 ]]; then COMPOSER_VERSION="--${COMPOSER_VERSION}"; else COMPOSER_VERSION="-- ${COMPOSER_VERSION}"; fi; fi; \
  composer self-update && composer self-update ${COMPOSER_VERSION} && composer --version

USER wodby
