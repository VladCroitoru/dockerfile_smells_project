FROM centos:6
LABEL maintainer="Matt Plachter"
ENV container=docker

# Install packages and other requirements.
RUN yum makecache fast \
 && yum -y update \
 && yum -y install \
      epel-release \
      initscripts \
      rsync \
      net-tools \
      python-argparse \
      sudo \
      which \
      wget \
 && yum clean all

RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

VOLUME ["/sys/fs/cgroup"]
CMD ["/sbin/init"]
