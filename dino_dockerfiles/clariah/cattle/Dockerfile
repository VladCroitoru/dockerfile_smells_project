FROM python:3.6.8
MAINTAINER albert.merono@vu.nl

ENV CATTLE_USER="cattle" \
    CATTLE_HOME="/home/cattle" \
    CATTLE_LOG_DIR="/var/log/cattle" \
    GITLAB_VERSION=8.10.4 \
    CATTLE_CACHE_DIR="/etc/docker-cattle"

ENV CATTLE_INSTALL_DIR="${CATTLE_HOME}/cattle" \
    CATTLE_DATA_DIR="${CATTLE_HOME}/data" \
    CATTLE_BUILD_DIR="${CATTLE_CACHE_DIR}/build" \
    CATTLE_RUNTIME_DIR="${CATTLE_CACHE_DIR}/runtime"

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y nginx git-core logrotate python-pip locales gettext-base sudo build-essential apt-utils \
 && update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \
 && locale-gen en_US.UTF-8 \
 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales \
 && rm -rf /var/lib/apt/lists/*

COPY ./ ${CATTLE_INSTALL_DIR}

COPY docker-assets/assets/build/ ${CATTLE_BUILD_DIR}/
RUN bash ${CATTLE_BUILD_DIR}/install.sh && rm -rf /var/lib/apt/lists/*

COPY docker-assets/assets/runtime/ ${CATTLE_RUNTIME_DIR}/
COPY docker-assets/entrypoint.sh /sbin/entrypoint.sh


RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 80/tcp

VOLUME ["${CATTLE_DATA_DIR}", "${CATTLE_LOG_DIR}"]
WORKDIR ${CATTLE_INSTALL_DIR}
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["app:start"]
