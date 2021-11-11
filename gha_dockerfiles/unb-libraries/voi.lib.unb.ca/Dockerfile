FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-redis
ENV DRUPAL_SITE_ID voi
ENV DRUPAL_SITE_URI voi.lib.unb.ca
ENV DRUPAL_SITE_UUID 87375ebe-f3d5-4681-b0ca-5e1352a52f83

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
COPY ./custom/splash  ${DRUPAL_ROOT}/splash

# Container metadata.
LABEL ca.unb.lib.generator="drupal9" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.description="voi.lib.unb.ca is the digital home for the bilingual research project, 'Vocabularies of Identity II'" \
  org.label-schema.name="voi.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://voi.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/voi.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/voi.lib.unb.ca"
