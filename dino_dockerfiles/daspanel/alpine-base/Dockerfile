FROM alpine:3.5
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Parse arguments for the build command.
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE

# Set default env variables
ENV \
    # Stop container initialization if error occurs in cont-init.d, fix-attrs.d script's
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \

    # Timezone
    TZ="UTC" \

    # S6 overlay version
    S6_OVERLAY_VERSION=v1.19.1.1 \

    # DASPANEL defaults
    DASPANEL_WAIT_FOR_API="YES"

# A little bit of metadata management.
# See http://label-schema.org/  
LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vendor="DASPANEL" \
      org.label-schema.version=$VERSION \
      org.label-schema.url="http://daspanel.com" \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="alpine-base" \
      org.label-schema.description="Base image for Daspanel projects" \
      org.label-schema.architecture="x86_64" \
      org.label-schema.distribution="Alpine Linux" \
      org.label-schema.distribution-version="3.5" 

RUN set -x \

    # This folder is in $PATH by default but isn't created by default
    && mkdir -p /usr/local/sbin \

    # Install minimal packages
    && apk add --update --no-cache ca-certificates wget ssmtp 'su-exec>=0.2' \

    # Install s6 overlay
    && wget https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz --no-check-certificate -O /tmp/s6-overlay.tar.gz \
    && tar xvfz /tmp/s6-overlay.tar.gz -C / \
    && rm -f /tmp/s6-overlay.tar.gz \

    # Install gomplate
    && wget https://github.com/hairyhenderson/gomplate/releases/download/v1.9.1/gomplate_linux-amd64-slim -O /usr/bin/gomplate \
    && chmod 755 /usr/bin/gomplate \

    # Clean image space
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/*

# Inject files in container file system
COPY rootfs /

ENTRYPOINT ["/init"]
CMD []


