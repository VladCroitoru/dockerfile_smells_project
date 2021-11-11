#
# Name: Wake on Lan
#
# Description:
# Application that sends the Wake-on-LAN magic packet to a computer in
# order to wake him up from slumber.
#
FROM gliderlabs/alpine:3.4
MAINTAINER Andy Savage <andy@savage.hk>

ARG WOL_PY_REPO="stevenaubertin/wol.py"
ARG WOL_LOCAL_DIR="/opt/python-wol"
ENV WOL_LOCAL_DIR ${WOL_LOCAL_DIR}

# By default we want to check every 5 minutes
ENV CRON_CHECK_INTERVAL "*/5 * * * *"
ENV HOSTS_TO_WAKE "192.168.1.3/70:85:c2:38:71:f4"
ENV MAC_ADDRS_FILE "/data/macs"
ENV BROADCAST_NETWORK "255.255.255.255"
ENV DESTINATION_PORT 9

ENV VERBOSE "yes"
ENV TZ "Asia/Hong_Kong"

WORKDIR /

RUN set -ex \
  && apk add --no-cache \
            bash \
            python \
            py-pip \
  && apk add --no-cache \
             --virtual TMP \
            curl \
            ca-certificates \
            tar \
            jq

# Install Awake
RUN pip install --upgrade pip awake

# Get the latest s6 overlay
RUN VERSION=`curl -s https://api.github.com/repos/just-containers/s6-overlay/releases/latest | jq -r ".tag_name"` \
    && curl -sSL "https://github.com/just-containers/s6-overlay/releases/download/${VERSION}/s6-overlay-amd64.tar.gz" \
    | tar xzf - -C /
RUN sed -i "s/s6-nuke -th/s6-nuke -t/" /etc/s6/init/init-stage3

# Cleanup files
RUN apk del TMP \
    && rm -rfv /tmp/*

COPY root/ /

ENTRYPOINT ["/init"]
