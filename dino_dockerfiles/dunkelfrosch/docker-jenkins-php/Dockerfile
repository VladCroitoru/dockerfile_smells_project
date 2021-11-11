#
# -- SODEF --
#
# BUILD    : DF/[SERVICE][JENKINS][PHP]
# OS/CORE  : debian:8
# SERVICES : jenkins 2.7.4
#
# VERSION 0.9.6
#

FROM jenkins:2.7.4

MAINTAINER Patrick Paechnatz <patrick.paechnatz@gmail.com>
LABEL com.container.vendor="dunkelfrosch impersonate" \
      com.container.service="df/service/jenkins/php" \
      com.container.priority="1" \
      com.container.project="df-service-jenkins-php" \
      img.version="0.9.6" \
      img.name="local/df/service/jenkins/php" \
      img.description="jenkins ci service image for dynamic slave build using kubernetes"

# setup some system required environment variables
ENV TIMEZONE           "Europe/Berlin"
ENV TERM                xterm-color
ENV LC_ALL              C
ENV LANG                en_US.UTF-8
ENV NCURSES_NO_UTF8_ACS 1

# setup some internal environment variables
ENV _GOSU_VERSION       1.9

# start processing as root
USER root

# prepare main remote docker helper script path
RUN mkdir -p /opt/docker

# copy docker script debian cleanup file to docker image
ADD https://raw.githubusercontent.com/dunkelfrosch/docker-bash/master/docker_cleanup_debian.sh /opt/docker/

# x-layer 1: package manager related processor
RUN apt-get update -qq >/dev/null 2>&1 \
    && apt-get install -qq -y --no-install-recommends mc wget curl ntp sudo >/dev/null 2>&1

# x-layer 2: update jenkins sudo bound
RUN echo "jenkins ALL=NOPASSWD: ALL" > /etc/sudoers

# x-layer 3: system core setup related processor
RUN set -e \
    && echo "${TIMEZONE}" >/etc/timezone \
    && dpkg-reconfigure tzdata >/dev/null 2>&1

# x-layer 4: install gosu (simple go-based setuid+setgid+setgroups+exec)
RUN set -e \
  && gpg --keyserver pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
  && curl -sSL -o /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/${_GOSU_VERSION}/gosu-$(dpkg --print-architecture)" \
  && curl -sSL -o /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/${_GOSU_VERSION}/gosu-$(dpkg --print-architecture).asc" \
  && gpg --verify /usr/local/bin/gosu.asc \
  && rm /usr/local/bin/gosu.asc \
  && chmod +x /usr/local/bin/gosu

# x-layer 5: install required plugins
RUN set -e \
    && /usr/local/bin/install-plugins.sh durable-task:1.12 credentials:2.1.4 kubernetes:0.8

# x-layer 6: provide new entrypoint
COPY ./entrypoint.sh /opt/docker/entrypoint.sh

# x-layer 7: add executable bit to entrypoint script
RUN chmod +x /opt/docker/entrypoint.sh

# x-layer 8: remove executors in jenkins master
COPY ./opt/docker/master-executors.groovy /usr/share/jenkins/ref/init.groovy.d/

# x-layer 9: build script cleanUp related processor
RUN set -e \
    && sh /opt/docker/docker_cleanup_debian.sh

#
# -- EODEF --
#

ENTRYPOINT ["/bin/tini", "--", "/opt/docker/entrypoint.sh"]