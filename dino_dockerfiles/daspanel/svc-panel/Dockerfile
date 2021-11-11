FROM alpine:3.6
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Parse Daspanel common arguments for the build command.
ARG VERSION
ARG VCS_URL
ARG VCS_REF
ARG BUILD_DATE
ARG S6_OVERLAY_VERSION=v1.19.1.1
ARG DASPANEL_IMG_NAME=svc-panel
ARG DASPANEL_OS_VERSION=alpine3.6
ARG PYTHON_VERSION=2.7

# Parse Container specific arguments for the build command.
#ARG CADDY_PLUGINS="http.cors,http.expires,http.ipfilter,http.ratelimit,http.realip"
#ARG CADDY_URL="https://caddyserver.com/download/linux/amd64?plugins=${CADDY_PLUGINS}"
ARG INSTALL_PATH=/opt/daspanel/apps/panel

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
      org.label-schema.name="daspanel/svc-panel" \
      org.label-schema.description="Docker container running Daspanel web panel server."

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

    # Install Python
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/10_install_python${PYTHON_VERSION} \

    # Install build environment packages
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/00_buildenv${PYTHON_VERSION} \

    # Install pyCurl
    && export PYCURL_SSL_LIBRARY=openssl \
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/20_pip${PYTHON_VERSION}_install "--compile pycurl==7.43.0" \

    # Install basic python packages used by Daspanel
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/20_pip${PYTHON_VERSION}_install "gunicorn==19.7.1 setproctitle gevent" \

    # Install software
    && mkdir -p ${INSTALL_PATH} \
    && wget --no-check-certificate -O /tmp/panel-src.zip https://github.com/daspanel/panel/archive/master.zip \
    && unzip -o -d /tmp /tmp/panel-src.zip \
    && mv /tmp/panel-master/daspanel_web ${INSTALL_PATH}/. \
    && mv /tmp/panel-master/requirements.txt ${INSTALL_PATH}/. \

    # Install pip packages needed by the software
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/20_pip${PYTHON_VERSION}_install "-r ${INSTALL_PATH}/requirements.txt " \

    # Remove build environment packages
    && sh /opt/daspanel/bootstrap/${DASPANEL_OS_VERSION}/${DASPANEL_IMG_NAME}/09_cleanbuildenv \

    # Install Caddy
    #&& curl --silent --show-error --fail --location \
    #    --header "Accept: application/tar+gzip, application/x-gzip, application/octet-stream" -o - \
    #    "${CADDY_URL}" \
    #    | tar --no-same-owner -C /usr/sbin/ -xz caddy \
    #&& chmod 0755 /usr/sbin/caddy \
    #&& setcap "cap_net_bind_service=+ep" /usr/sbin/caddy \

    # Cleanup
    && rm -rf /tmp/* \
    && rm -rf /var/cache/apk/*

# Let's S6 control the init system
ENTRYPOINT ["/init"]
CMD []

# Expose ports for the service
EXPOSE 8080

