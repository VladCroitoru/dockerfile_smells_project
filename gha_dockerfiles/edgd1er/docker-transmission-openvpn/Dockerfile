# syntax=docker/dockerfile:1
FROM alpine:3.14 as TransmissionUIs

#SHELL ["/bin/bash", "-o", "pipefail", "-c"]
#hadolint ignore=DL3018
RUN apk --no-cache add wget jq bash\
    && mkdir -p /opt/transmission-ui \
    && echo "Install Shift" \
    && wget --no-cache -qO- https://github.com/killemov/Shift/archive/master.tar.gz | tar xz -C /opt/transmission-ui \
    && mv /opt/transmission-ui/Shift-master /opt/transmission-ui/shift \
    && echo "Install Flood for Transmission" \
    && wget --no-cache -qO- https://github.com/johman10/flood-for-transmission/releases/download/latest/flood-for-transmission.tar.gz | tar xz -C /opt/transmission-ui \
    && echo "Install Combustion" \
    && wget --no-cache -qO- https://github.com/Secretmapper/combustion/archive/release.tar.gz | tar xz -C /opt/transmission-ui \
    && echo "Install kettu" \
    && wget --no-cache -qO- https://github.com/endor/kettu/archive/master.tar.gz | tar xz -C /opt/transmission-ui \
    && mv /opt/transmission-ui/kettu-master /opt/transmission-ui/kettu \
    && echo "Install Transmission-Web-Control" \
    && mkdir /opt/transmission-ui/transmission-web-control \
    && wget --no-cache -qO- "$(wget --no-cache -qO- https://api.github.com/repos/ronggang/transmission-web-control/releases/latest | jq --raw-output '.tarball_url')" | tar -C /opt/transmission-ui/transmission-web-control/ --strip-components=2 -xz

FROM debian:buster-slim

VOLUME /data
VOLUME /config

COPY --from=TransmissionUIs /opt/transmission-ui /opt/transmission-ui

ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
#hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && \
    apt-add-repository non-free && apt-get update && apt-get install -y --no-install-recommends \
    dumb-init openvpn transmission-daemon transmission-cli privoxy telnet procps \
    tzdata dnsutils iputils-ping ufw openssh-client git jq curl wget unrar unzip bc \
    && ln -s /usr/share/transmission/web/style /opt/transmission-ui/transmission-web-control \
    && ln -s /usr/share/transmission/web/images /opt/transmission-ui/transmission-web-control \
    && ln -s /usr/share/transmission/web/javascript /opt/transmission-ui/transmission-web-control \
    && ln -s /usr/share/transmission/web/index.html /opt/transmission-ui/transmission-web-control/index.original.html \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* \
    && groupmod -g 1000 users \
    && useradd -u 911 -U -d /config -s /bin/false abc \
    && usermod -G users abc


# Add configuration and scripts
COPY openvpn/ /etc/openvpn/
COPY transmission/ /etc/transmission/
COPY scripts /etc/scripts/
COPY privoxy/scripts /opt/privoxy/
#Add a script to test dnsleeak https://raw.githubusercontent.com/macvk/dnsleaktest/master/dnsleaktest.sh
#ADD https://raw.githubusercontent.com/macvk/dnsleaktest/master/dnsleaktest.sh /etc/scripts/

ENV OPENVPN_USERNAME=**None** \
    OPENVPN_PASSWORD=**None** \
    OPENVPN_PROVIDER=**None** \
    GLOBAL_APPLY_PERMISSIONS=true \
    TRANSMISSION_HOME=/data/transmission-home \
    TRANSMISSION_RPC_PORT=9091 \
    TRANSMISSION_DOWNLOAD_DIR=/data/completed \
    TRANSMISSION_INCOMPLETE_DIR=/data/incomplete \
    TRANSMISSION_WATCH_DIR=/data/watch \
    CREATE_TUN_DEVICE=true \
    ENABLE_UFW=false \
    UFW_ALLOW_GW_NET=false \
    UFW_EXTRA_PORTS= \
    UFW_DISABLE_IPTABLES_REJECT=false \
    PUID= \
    PGID= \
    PEER_DNS=true \
    PEER_DNS_PIN_ROUTES=true \
    DROP_DEFAULT_ROUTE= \
    WEBPROXY_ENABLED=false \
    WEBPROXY_PORT=8118 \
    WEBPROXY_USERNAME= \
    WEBPROXY_PASSWORD= \
    LOG_TO_STDOUT=false \
    HEALTH_CHECK_HOST=google.com \
    SELFHEAL=false

HEALTHCHECK --start-period=10s --interval=1m CMD /etc/scripts/healthcheck.sh

# Add labels to identify this image and version
ARG REVISION
# Set env from build argument or default to empty string
ENV REVISION=${REVISION:-""}
LABEL org.opencontainers.image.source=https://github.com/haugene/docker-transmission-openvpn
LABEL org.opencontainers.image.revision=$REVISION

# Compatability with https://hub.docker.com/r/willfarrell/autoheal/
LABEL autoheal=true

# Expose port and run
#Transmission-RPC
EXPOSE 9091
# Privoxy
EXPOSE 8118

CMD ["dumb-init", "/etc/openvpn/start.sh"]
