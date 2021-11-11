FROM debian:8
LABEL maintainer="Matt Plachter"
ENV container=docker

RUN find /etc/systemd/system \
         /lib/systemd/system \
         -path '*.wants/*' \
         -not -name '*journald*' \
         -not -name '*systemd-tmpfiles*' \
         -not -name '*systemd-user-sessions*' \
         -exec rm \{} \;

# Install requirements.
RUN apt-get -y update \
 && apt-get -y install \
      apt-utils \
      initscripts \
      rsync \
      net-tools \
      python-argparse \
      sudo \
      apt-transport-https \
      curl \
      vim \
      wget \
 && apt-get clean all

RUN systemctl set-default multi-user.target

VOLUME ["/sys/fs/cgroup"]
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]
