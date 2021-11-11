FROM ghcr.io/unb-libraries/drupal:8.x-3.x-unblib
MAINTAINER UNB Libraries <libsupport@unb.ca>

# Install additional OS packages.
ENV ADDITIONAL_OS_PACKAGES tiff-dev tiff postfix imagemagick bash openssh-client php7-redis
ENV DRUPAL_SITE_ID unbherb
ENV DRUPAL_SITE_URI unbherbarium.lib.unb.ca
ENV DRUPAL_SITE_UUID 85c96bf2-f1b6-4612-8305-d3d3769d5255

ENV DRUPAL_PRIVATE_FILE_PATH /app/private_filesystem
ENV GIT_LFS_VERSION 2.7.2

# Build application.
COPY ./build/ /build/
RUN ${RSYNC_MOVE} /build/scripts/container/ /scripts/ && \
  /scripts/addOsPackages.sh && \
  /scripts/setupStandardConf.sh && \
  curl -O https://raw.githubusercontent.com/VoidVolker/MagickSlicer/master/magick-slicer.sh && \
  mv magick-slicer.sh /usr/local/bin/magick-slicer && \
  chmod +x /usr/local/bin/magick-slicer && \
  /scripts/InstallGitLFS.sh && \
  /scripts/build.sh

# Deploy custom assets, configuration.
COPY ./config-yml ${DRUPAL_CONFIGURATION_DIR}
COPY ./custom/themes ${DRUPAL_ROOT}/themes/custom
COPY ./custom/modules ${DRUPAL_ROOT}/modules/custom

# Container metadata.
LABEL ca.unb.lib.generator="drupal8" \
  com.microscaling.docker.dockerfile="/Dockerfile" \
  com.microscaling.license="MIT" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.description="unbherbarium.lib.unb.ca provides a searchable database of the vascular plant collections maintained at the  Connell Memorial Herbarium, and in-depth information about its policies, facilities and collections." \
  org.label-schema.name="unbherbarium.lib.unb.ca" \
  org.label-schema.schema-version="1.0" \
  org.label-schema.url="https://unbherbarium.lib.unb.ca" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/unb-libraries/unbherbarium.lib.unb.ca" \
  org.label-schema.vendor="University of New Brunswick Libraries" \
  org.label-schema.version=$VERSION \
  org.opencontainers.image.source="https://github.com/unb-libraries/unbherbarium.lib.unb.ca"
