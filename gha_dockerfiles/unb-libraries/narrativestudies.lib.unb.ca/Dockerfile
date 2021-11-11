FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-redis
ENV DRUPAL_SITE_ID narrativ
ENV DRUPAL_SITE_URI narrativestudies.lib.unb.ca
ENV DRUPAL_SITE_UUID 505198c5-b3da-4759-80ae-8f2bcfb469b5

# Build application.
COPY ./build/ /build/
RUN ${RSYNC_MOVE} /build/scripts/container/ /scripts/ && \
  /scripts/addOsPackages.sh && \
  /scripts/initOpenLdap.sh && \
  /scripts/setupStandardConf.sh && \
  /scripts/build.sh

# Deploy custom assets, configuration.
COPY ./config-yml ${DRUPAL_CONFIGURATION_DIR}
COPY ./custom/themes ${DRUPAL_ROOT}/themes/custom
COPY ./custom/modules ${DRUPAL_ROOT}/modules/custom

# Container metadata.
LABEL ca.unb.lib.generator="drupal9" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.description="narrativestudies.lib.unb.ca a searchable bibliography of books, articles, and other resources that are relevant to narrative, directly or otherwise, in a broad range of disciplines and fields." \
  org.label-schema.name="narrativestudies.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://narrativestudies.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/narrativestudies.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/narrativestudies.lib.unb.ca"
