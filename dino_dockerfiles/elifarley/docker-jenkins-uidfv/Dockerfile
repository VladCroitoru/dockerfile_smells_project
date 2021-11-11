FROM jenkins/jenkins:lts-alpine
MAINTAINER Elifarley Cruz <elifarley@gmail.com>

ENV BASE_IMAGE=jenkins/jenkins:lts-alpine

ARG APK_PACKAGES="su-exec shadow"

ARG MNT_DIR=/var/jenkins_home
ARG _USER=jenkins
ARG HOME="$MNT_DIR"
ARG TZ=Brazil/East
ARG JAVA_TOOL_OPTIONS="-Duser.timezone=$TZ"
ARG TERM=xterm-256color

ENV \
  MNT_DIR="$MNT_DIR" \
  _USER="$_USER" \
  HOME="$HOME" \
  TZ="$TZ" \
  JAVA_TOOL_OPTIONS="$JAVA_TOOL_OPTIONS" \
  TERM="$TERM"

ENTRYPOINT ["tini", "--", "entrypoint"]
CMD ["/usr/local/bin/jenkins.sh"]

WORKDIR $HOME

USER root

RUN curl -fsSL https://raw.githubusercontent.com/elifarley/cross-installer/master/install.sh | sh && \
  xinstall save-image-info && \
  xinstall add entrypoint && \
  xinstall add timezone && \
  DEBUG=1 xinstall add-pkg && \
  xinstall cleanup && \
  _f=/usr/local/bin/install-plugins-custom.sh && \
  printf '#!/bin/sh\nREF="${1:-$JENKINS_HOME/plugins}"; test $# -gt 0 && shift\nREF="$REF" exec install-plugins.sh "$@"\n' > "$_f" && \
  chmod +x "$_f"

# See https://github.com/bdruemen/jenkins-docker-uid-from-volume/blob/master/Dockerfile
# Modify the UID of the jenkins user to automatically match the mounted volume.
# Use it just like the original: https://hub.docker.com/_/jenkins/
