FROM alpine:3.6
MAINTAINER Clint Beacock <clint@therefore.ca>

ENV HENCE_PREFIX=/opt/hence \
    HENCE_USER=hence

COPY rootfs /

# Add common packages and create hence user and added specific requirements
RUN echo "http://nl.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk add --update \
  ca-certificates \
  curl \
  bash \
  bash-completion \
  ncurses \
  vim \
  tree \
  tar \
  shadow \
  rsync \
  sudo \
  gettext \
  execline@edge && \
  rm -rf /var/cache/apk/* && \
  curl -R -L -O https://github.com/just-containers/s6-overlay/releases/download/v1.13.0.0/s6-overlay-amd64.tar.gz && \
  tar xvfz s6-overlay-amd64.tar.gz -C / && \
  printf '#!/bin/bash\n. $HENCE_PREFIX/hence-utils.sh\nprint_hence_help_page' > '/usr/bin/print-help' && \
  printf '#!/bin/bash\n. $HENCE_PREFIX/hence-utils.sh\ncheck_for_updates' > '/usr/bin/check-updates' && \
  chmod a+x /usr/bin/print-help /usr/bin/check-updates && \
  adduser $HENCE_USER -D -g "" && \
  sed -i -e 's/\s*Defaults\s*secure_path\s*=/# Defaults secure_path=/' /etc/sudoers && \
  echo "hence ALL=NOPASSWD: ALL" >> /etc/sudoers

COPY install.sh $HENCE_PREFIX/install.sh
COPY hence-utils.sh $HENCE_PREFIX/hence-utils.sh

ENTRYPOINT ["/init"]

CMD []
