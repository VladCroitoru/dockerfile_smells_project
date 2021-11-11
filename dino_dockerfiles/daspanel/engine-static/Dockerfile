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

FROM daspanel/engine-base-dev:dev
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Copy bynaries build before
COPY --from=builder-caddy /caddy-build/caddy /usr/sbin/caddy

# Parse Daspanel common arguments for the build command.
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE
ARG S6_OVERLAY_VERSION=v1.21.4.0
ARG DASPANEL_IMG_NAME=engine-static
ARG DASPANEL_OS_VERSION=alpine3.6

# Parse Container specific arguments for the build command.
ARG GOTTY_URL="https://github.com/yudai/gotty/releases/download/v2.0.0-alpha.3/gotty_2.0.0-alpha.3_linux_amd64.tar.gz"

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
      org.label-schema.name="daspanel/engine-static" \
      org.label-schema.description="This service provides HTTP static engine server to Daspanel sites."

ENV TERM=xterm-256color
ENV VAR_PREFIX=/var/run
ENV LOG_PREFIX=/var/log/caddy
ENV TEMP_PREFIX=/tmp
ENV CACHE_PREFIX=/var/cache

# Solves: https://github.com/wp-cli/wp-cli/issues/4246#issuecomment-325774849
# less: unrecognized option: r
# BusyBox v1.26.2 (2017-06-11 06:38:32 GMT) multi-call binary.
ENV PAGER='more' 

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

    # Install specific OS packages needed by this image
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/99_install_pkgs "git zip python3 python3-dev mariadb-dev" \
    && python3 -m ensurepip \
    && rm -r /usr/lib/python*/ensurepip \
    && pip3 install --no-cache-dir --upgrade pip setuptools \
    && pip3 install pipenv \

    # Install gotty
    && curl --progress-bar --show-error --fail --location \
        --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o /tmp/gotty.tar.gz \
        "${GOTTY_URL}" \
    && tar -C /usr/sbin -xvzf /tmp/gotty.tar.gz \
    && chmod 0755 /usr/sbin/gotty \
    && mkdir /lib64 \
    && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \
    && rm /tmp/gotty.tar.gz \

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
EXPOSE 443

