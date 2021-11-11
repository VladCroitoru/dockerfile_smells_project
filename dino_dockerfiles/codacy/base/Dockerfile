FROM adoptopenjdk/openjdk8:jdk8u302-b08-ubuntu-slim@sha256:e1f78e2ea4ba1adc8c03eda94a45a4d667bdb19f991700a56600d8a85694c425

LABEL maintainer="Codacy Team <code@codacy.com>"

RUN \
  apt-get -y update && \
  apt-get -y install software-properties-common gnupg && \
  export GNUPGHOME="$(mktemp -d)" && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A1715D88E1DF1F24 && \
  add-apt-repository -y "deb http://ppa.launchpad.net/git-core/ppa/ubuntu focal main" && \
  apt-get -y update && \
  apt-get -y install wget unzip && \
  apt-get -y install git=1:2.* && \
  rm -rf "$GNUPGHOME" && \
  apt-get -y remove software-properties-common gnupg && \
  rm -rf /root/.cache && \
  apt-get purge -y $(apt-cache search '~c' | awk '{ print $2 }') && \
  apt-get -y autoremove && \
  apt-get -y autoclean && \
  apt-get -y clean all && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/apt && \
  rm -rf /tmp/*

# Git and SSH Configs
RUN \
  echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \
  git config --global core.quotepath false && \
  git config --global core.packedGitLimit 512m && \
  git config --global core.packedGitWindowSize 512m && \
  git config --global pack.deltaCacheSize 2047m && \
  git config --global pack.packSizeLimit 2047m && \
  git config --global pack.windowMemory 2047m

# Docker 17.09.0 binary
# Used for cloud and enterprise before kubernetes in:
#  - https://bitbucket.org/qamine/worker-manager/src/a24392951fb84c3551a007cf8128eed2ada9e7e2/conf/reference.conf#lines-238
#  - https://bitbucket.org/qamine/codacy-doplicated/src/954dd8e7c9c28bdea0143682cc2fe21a0e878cdd/variables/conf.dockerversion.json#lines-5
RUN \
  DOCKER_VERSION="docker-17.09.0-ce" && \
  wget https://download.docker.com/linux/static/stable/x86_64/$DOCKER_VERSION.tgz && \
  tar -xvf $DOCKER_VERSION.tgz --strip-components 1 docker/docker && \
  rm -rf $DOCKER_VERSION.tgz && \
  mv docker /usr/bin/$DOCKER_VERSION && \
  chmod +x /usr/bin/$DOCKER_VERSION

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
