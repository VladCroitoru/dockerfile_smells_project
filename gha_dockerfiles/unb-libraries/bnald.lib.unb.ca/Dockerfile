FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-xmlreader php7-zip imagemagick php7-redis
ENV DRUPAL_SITE_ID bnald
ENV DRUPAL_SITE_URI bnald.lib.unb.ca
ENV DRUPAL_SITE_UUID c8857708-03ab-4f57-beeb-a60bd827e72f

# Build application.
COPY ./build/ /build/
RUN ${RSYNC_MOVE} /build/scripts/container/ /scripts/ && \
  /scripts/addOsPackages.sh && \
  /scripts/initOpenLdap.sh && \
  /scripts/setupStandardConf.sh

RUN /scripts/build.sh

# Deploy custom assets, configuration.
COPY ./config-yml ${DRUPAL_CONFIGURATION_DIR}
COPY ./custom/themes ${DRUPAL_ROOT}/themes/custom
COPY ./custom/modules ${DRUPAL_ROOT}/modules/custom

# Container metadata.
LABEL ca.unb.lib.generator="drupal9" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.description="bnald.lib.unb.ca provides an archive for characteristics of all the legislation passed by the pre-Confederation assemblies of eastern British North America." \
  org.label-schema.name="bnald.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://bnald.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/bnald.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/bnald.lib.unb.ca"
