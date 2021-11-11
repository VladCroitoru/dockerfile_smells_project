FROM golang:1.9-alpine3.6 as builder-caddy
LABEL maintainer="ulrich.schreiner@gmail.com"

ENV CADDY_VERSION v0.10.10

# Inject files in container file system
COPY caddy-build /caddy-build

RUN apk --no-cache update \
    && apk --no-cache --update add git bash \
    && cd /caddy-build \
    && env OS=linux ARCH=amd64 ./build_caddy.sh \
    && ls -la /caddy-build/caddy

FROM alpine:3.6
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Copy bynaries build before
COPY --from=builder-caddy /caddy-build/caddy /usr/sbin/caddy

# Parse Daspanel common arguments for the build command.
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE
ARG S6_OVERLAY_VERSION=v1.19.1.1
ARG DASPANEL_IMG_NAME=load-balancer-caddy
ARG DASPANEL_OS_VERSION=alpine3.6

# Set default env variables
ENV \
    # Stop container initialization if error occurs in cont-init.d, fix-attrs.d script's
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \

    # Timezone
    TZ="UTC" \

    # DASPANEL defaults
    DASPANEL_WAIT_FOR_API="YES"

# A little bit of metadata management.
# See http://label-schema.org/  
LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$VERSION \
      org.label-schema.vcs-url=$VCS_URL \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.name="load-balancer-caddy" \
      org.label-schema.description="This service provides HTTP load balancer to Daspanel sites."


# Inject files in container file system
COPY rootfs /

RUN set -x \

    # Initial OS bootstrap - required
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/00_base \

    # Install Daspanel base - common layer for all container's independent of the OS and init system
    && wget -O /tmp/opt-daspanel.zip "https://github.com/daspanel/rootfs-base/releases/download/0.1.0/opt-daspanel.zip" \
    && unzip -o -d / /tmp/opt-daspanel.zip \

    # Install Daspanel bootstrap for Alpine Linux with S6 Overlay Init system
    && wget -O /tmp/alpine-s6.zip "https://github.com/daspanel/rootfs-base/releases/download/0.1.0/alpine-s6.zip" \
    && unzip -o -d / /tmp/alpine-s6.zip \

    # Bootstrap the system (TBD)

    # Install s6 overlay init system
    && wget https://github.com/just-containers/s6-overlay/releases/download/$S6_OVERLAY_VERSION/s6-overlay-amd64.tar.gz --no-check-certificate -O /tmp/s6-overlay.tar.gz \
    && tar xvfz /tmp/s6-overlay.tar.gz -C / \
    && rm -f /tmp/s6-overlay.tar.gz \

    # Install Caddy
    && chmod 0755 /usr/sbin/caddy \
    && setcap "cap_net_bind_service=+ep" /usr/sbin/caddy \

    # Cleanup
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*

# Let's S6 control the init system
ENTRYPOINT ["/init"]
CMD []

# Expose ports for the service
EXPOSE 80 443
