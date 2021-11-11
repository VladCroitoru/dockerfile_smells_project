# MIT License
#
# Copyright (c) [2017] [Volker Machon]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM alpine:3.5
MAINTAINER Volker Machon <volker@machon.biz>

ARG BUSY_BOX_VERSION=1.26.2
ENV NODE_DISABLE_COLORS=1

COPY rootfs/ /
WORKDIR /opt/registrator
RUN mkdir -p /opt/registrator \
      && [ $(getent group registrator) ] || addgroup -S registrator \
      && [ $(getent passwd registrator) ] || adduser -h /opt/registrator -S -D -G registrator registrator \
      && apk add --no-cache \
             ca-certificates \
             nodejs \
      && npm install \
      && apk add --no-cache \
              gcc \
              make \
              musl-dev \
              ncurses-dev \
              openssl \
      && wget -O- https://busybox.net/downloads/busybox-${BUSY_BOX_VERSION}.tar.bz2 > /tmp/busybox.tar.bz2 \
      && cd /tmp \
      && tar xfj busybox.tar.bz2 \
      && cd busybox-${BUSY_BOX_VERSION} \
      && mv /busybox-config ./.config \
      && make \
      && chown -R registrator.registrator /opt/registrator \
      && for DEL_SYM_LINK in $(/bin/busybox find / -type l | /bin/busybox grep bin); do /bin/busybox rm ${DEL_SYM_LINK}; done \
      && for SYM_LINK in /bin/test /bin/[ /bin/[[ /bin/ps /bin/ash /bin/sh; do /bin/busybox ln -s /bin/busybox ${SYM_LINK}; done \
      && apk del \
             apk-tools \
             gcc \
             make \
             musl-dev \
             ncurses-dev \
             openssl \
      && /bin/busybox mv /tmp/busybox-${BUSY_BOX_VERSION}/busybox /bin/busybox.new \
      && /bin/busybox rm -rf /tmp/busybox* \
      && for DEL_USER in $(/bin/busybox grep -v registrator /etc/passwd | /bin/busybox awk -F':' '{print $1}'); do /bin/busybox deluser ${DEL_USER}; done \
      && /bin/busybox mv /bin/busybox.new /bin/busybox

USER registrator
# Healthcheck
HEALTHCHECK CMD node ping.js
ENTRYPOINT ["/entrypoint.sh"]
CMD ["registrator"]
