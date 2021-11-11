FROM debian:7
LABEL maintainer="Matt Plachter"
ENV container=docker

RUN rm /sbin/initctl
RUN dpkg-divert --local --rename --remove /sbin/initctl

# Install requirements.
RUN apt-get -y update
RUN apt-get -y install \
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


VOLUME ["/sys/fs/cgroup"]
CMD ["/bin/bash", "-c", "exec /sbin/init --log-target=journal 3>&1"]
