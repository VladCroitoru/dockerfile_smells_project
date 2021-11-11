FROM dexec/bash
MAINTAINER Maikel Wever <maikelwever@gmail.com>

VOLUME /build
WORKDIR /build

# Fix /etc/makepkg.conf
RUN mkdir -p /etc
ADD makepkg.conf /etc/makepkg.conf

# Copy over buildscript
ADD parsepkgbuild.sh /opt/parsepkgbuild.sh

# Options: Install dependencies, force package build, clean afterwards
ENTRYPOINT bash /opt/parsepkgbuild.sh
