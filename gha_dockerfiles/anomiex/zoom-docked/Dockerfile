FROM debian:bullseye-slim
MAINTAINER Brad Jorsch <anomie@users.sourceforge.net>

ARG DEBIAN_FRONTEND=noninteractive
ARG ZOOM_URL=https://zoom.us/client/latest/zoom_amd64.deb

RUN \
  printf "\e[7m== Installing curl ==\e[0m\n" && \
  apt-get update && \
  apt-get -y install curl && \
  \
  printf "\e[7m== Downloading Zoom ==\e[0m\n" && \
  curl -L $ZOOM_URL -o /tmp/zoom_setup.deb && \
  \
  printf "\e[7m== Removing curl ==\e[0m\n" && \
  apt-get --purge --auto-remove -y remove curl && \
  \
  printf "\e[7m== Installing Zoom and utilities ==\e[0m\n" && \
  apt-get -y install sudo zenity xclip dbus-x11 /tmp/zoom_setup.deb && \
  dpkg --field /tmp/zoom_setup.deb Version > /etc/zoom-version && \
  \
  printf "\e[7m== Cleaning up ==\e[0m\n" && \
  rm -rf /tmp/zoom_setup.deb /var/lib/apt/lists/* && \
  # The symlink interferes with `-v /etc/localtime:/etc/localtime:ro` in the wrapper, so remove it.
  rm -f /etc/localtime && \
  \
  printf "\e[7m== Finishing build ==\e[0m\n"

COPY zoom-docked /var/scripts/zoom-docked
COPY bin/docker-exec.sh bin/docker-run.sh /sbin/
COPY bin/docker-shared.sh /usr/share/zoom-docked/
COPY bin/xdg-open /usr/bin/xdg-open
RUN chmod 0755 /sbin/docker-exec.sh /sbin/docker-run.sh /usr/bin/xdg-open

ENTRYPOINT ["/sbin/docker-run.sh"]
CMD ["help"]
