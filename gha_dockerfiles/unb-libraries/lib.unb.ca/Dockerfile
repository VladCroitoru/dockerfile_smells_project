FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-xmlreader php7-zip php7-redis php7-pear openssh-client
ENV DRUPAL_PRIVATE_FILE_PATH /app/private_filesystem
ENV DRUPAL_SITE_ID libweb
ENV DRUPAL_SITE_URI lib.unb.ca
ENV DRUPAL_SITE_UUID 87d22fc3-a2d0-4543-aab8-6ed800691b7b

# Build application.
COPY ./build/ /build/
RUN ${RSYNC_MOVE} /build/scripts/container/ /scripts/ && \
  ${RSYNC_MOVE} /build/keys/ /app/keys/ && \
  /scripts/addOsPackages.sh && \
  /scripts/initOpenLdap.sh && \
  /scripts/installFileMarc.sh && \
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
  org.label-schema.description="lib.unb.ca is the core web application at UNB Libraries." \
  org.label-schema.name="lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/lib.unb.ca"
