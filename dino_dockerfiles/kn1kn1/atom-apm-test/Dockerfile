# DESCRIPTION:
#   Install dependencies for the atom editor package testing `apm test`.
# AUTHOR: Kenichi Kanai <kn1kn1@users.noreply.github.com>
# USAGE:
#   See the usage in the actual package building.
#   https://github.com/kn1kn1/language-context-free/blob/master/Dockerfile

# Atom Docker Image For Package Testing
FROM ubuntu:trusty
MAINTAINER Kenichi Kanai <kn1kn1@users.noreply.github.com>

RUN \
# Make Sure We're Up To Date
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \
# Install Required Packages For Atom
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    gconf2 \
    gconf-service \
    libgtk2.0-0 \
    libnotify4 \
    libxtst6 \
    libnss3 \
    python \
    gvfs-bin \
    xdg-utils \
    libxss1 \
#  For downloading deb
    wget \
    ca-certificates \
#  For apm install
    make \
    g++ \
#  For apm test
    xvfb \
    libasound2 \
    --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
