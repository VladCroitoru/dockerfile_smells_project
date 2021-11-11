FROM sys42/docker-base:1.1.0
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>

RUN set -e   &&   set -x   &&   export LC_ALL=C              && \
export DEBIAN_FRONTEND=noninteractive                        && \
if [ ! -e /var/lib/apt/lists/lock ]; then apt-get update; fi && \
apt-get install -y --no-install-recommends build-essential   && \
apt-get install -y --no-install-recommends git               && \
apt-get install -y --no-install-recommends python            && \
apt-get clean                                                && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
