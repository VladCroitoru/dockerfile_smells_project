#FROM maikelwever/docker-archlinux:latest
FROM base/archlinux:latest
MAINTAINER Maikel Wever <maikelwever@gmail.com>

# Adding mirrorlist with Dutch servers for when I build locally
# Doesn't matter much on Docker Hub
ADD mirrorlist /etc/pacman.d/mirrorlist

RUN pacman -Syyu --needed --noconfirm base-devel sudo python-jinja git procps-ng
RUN bash -c "echo 'y\ny\n' | pacman -Scc"

VOLUME /build

# Set up user & sudo
ADD sudoers /etc/sudoers
RUN useradd -d /home/pellets/ -m -G wheel build && \
    chmod 0400 /etc/sudoers && \
    mkdir -p /home/pellets/ && \
    mkdir -p /build/ && \
    chown -R build:build /build && \
    chown -R build:build /home/pellets

# Copy over buildscript
ADD buildscript.py /opt/buildscript.py
WORKDIR /home/pellets/
USER build
ENV LANG en_US.utf8
ENTRYPOINT ["/usr/bin/python3", "/opt/buildscript.py"]
