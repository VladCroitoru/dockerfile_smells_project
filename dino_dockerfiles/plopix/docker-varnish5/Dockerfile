FROM debian:stretch-slim

# Inspired https://github.com/ezsystems/ezplatform/blob/master/doc/docker/Dockerfile-varnish
MAINTAINER Plopix

ENV VARNISH_MALLOC_SIZE "256M"
ENV DEBIAN_FRONTEND "noninteractive"
ENV VCL_CONFIG      "/etc/varnish/default.vcl"
ENV VARNISHD_PARAMS "-p default_ttl=3600 -p default_grace=3600 -p max_esi_depth=15 -p feature=+esi_disable_xml_check"

ARG PACKAGECLOUD_URL=https://packagecloud.io/install/repositories/varnishcache/varnish5/script.deb.sh
ARG VARNISH_MODULES_VERSION=0.12.1

COPY start.bash /start.bash

# Use official packages from Varnish and build with varnish-modules mainly for xkey
# see: https://github.com/varnish/varnish-modules/tree/master/docs
RUN set -xe \
        && buildDeps=" \
            make \
            automake \
            autotools-dev \
            libedit-dev \
            libjemalloc-dev \
            libncurses-dev \
            libpcre3-dev \
            libtool \
            pkg-config \
            python-docutils \
            python-sphinx \
            varnish-dev \
        " \
    # Update apt and get dependencies
        && apt-get update -q -y \
        && apt-get install -q -y --no-install-recommends ca-certificates curl bc net-tools \
        \
    # Get official Varnish package
        && curl -s ${PACKAGECLOUD_URL} | bash \
        && apt-get install -q -y --allow-unauthenticated --no-install-recommends varnish $buildDeps \
        \
    # Install varnish modules
        && curl -A "Docker" -o /tmp/varnish-modules.tar.gz -D - -L -s https://download.varnish-software.com/varnish-modules/varnish-modules-${VARNISH_MODULES_VERSION}.tar.gz \
        && tar zxpf /tmp/varnish-modules.tar.gz -C /tmp/ \
        && cd /tmp/varnish-modules-${VARNISH_MODULES_VERSION} \
        && ./configure \
        && make \
        # && make check \
        && make install \
        && rm -f /tmp/varnish-modules.tar.gz && rm -Rf /tmp/varnish-modules \
        \
    # Cleanup apt cache and remove build packages
        && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $buildDeps \
        && rm -rf /var/lib/apt/lists/*

EXPOSE 80 6082

CMD ["/start.bash"]
