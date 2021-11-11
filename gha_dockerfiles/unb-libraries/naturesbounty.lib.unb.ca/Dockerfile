FROM ghcr.io/unb-libraries/drupal:9.x-1.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES postfix php7-ldap php7-redis
ENV DRUPAL_SITE_ID nbounty
ENV DRUPAL_SITE_URI naturesbounty.lib.unb.ca
ENV DRUPAL_SITE_UUID 5386f767-6440-4d7e-8eb2-5578c3ae27c0

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
  org.label-schema.description="naturesbounty.lib.unb.ca outlines a study of plant exploration in New Brunswick from 1604 to 2000." \
  org.label-schema.name="naturesbounty.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://naturesbounty.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/naturesbounty.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/naturesbounty.lib.unb.ca"
