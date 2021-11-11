FROM centos:7

LABEL Name="centos-pod-pause" \
    Vendor="com.garethahealy" \
    Maintainer="garethahealy (https://github.com/garethahealy/)" \
    Version="1.0.1" \
    License="Apache License, Version 2.0"

USER root

ADD pause.c /pause-code/pause.c

# Install packages without docs. Variable is used to cause yum to fail if missing
RUN INSTALL_PKGS="gcc kernel-devel make" \
    && yum install -y $INSTALL_PKGS --setopt tsflags=nodocs \
    && rpm -V $INSTALL_PKGS \
    && rm -rf /var/cache/yum \
    && yum -y clean all

# Compile pause
RUN cd /pause-code && \
    cc -o pause pause.c

ENTRYPOINT ["/pause-code/pause"]
