# docker build -t brandfrisch/ubuntu-16.04:latest .
# docker run -it --privileged --rm=true -v $(pwd):/mnt/host brandfrisch/ubuntu-16.04:latest
FROM ubuntu:16.04

ENV container docker
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive

# Don't start any optional services except for the few we need.
RUN find /etc/systemd/system \
  /lib/systemd/system \
  -path '*.wants/*' \
  -not -name '*journald*' \
  -not -name '*systemd-tmpfiles*' \
  -not -name '*systemd-user-sessions*' \
  -exec rm \{} \;

# configure apt behaviour
RUN echo "APT::Get::Install-Recommends 'false'; \n\
  APT::Get::Install-Suggests 'false'; \n\
  APT::Get::Assume-Yes 'true'; \n\
  APT::Get::force-yes 'true';" > /etc/apt/apt.conf.d/00-general

RUN apt-get update
RUN apt-get install -yq dbus systemd apt-utils ssl-cert ca-certificates apt-transport-https curl wget git python sudo
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN systemctl set-default multi-user.target
RUN systemctl mask dev-hugepages.mount sys-fs-fuse-connections.mount

COPY setup /sbin/

STOPSIGNAL SIGRTMIN+3

# Workaround for docker/docker#27202, technique based on comments from docker/docker#9212
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]
