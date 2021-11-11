FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-xmlreader php7-zip php7-redis
ENV DRUPAL_SITE_ID newspapers
ENV DRUPAL_SITE_URI newspapers.lib.unb.ca
ENV DRUPAL_SITE_UUID 655af73f-dc1a-48f1-84a1-3da88d2d1ad4

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
  org.label-schema.description="newspapers.lib.unb.ca provides researchers with unified access to UNB Libraries' current and historical newspaper collections in all formats, from New Brunswick and across the world." \
  org.label-schema.name="newspapers.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://newspapers.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/newspapers.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/newspapers.lib.unb.ca"
