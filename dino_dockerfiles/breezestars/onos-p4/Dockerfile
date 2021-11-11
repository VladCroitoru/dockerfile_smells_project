FROM p4lang/p4app
MAINTAINER Jimmy Ou <breezestars@gmail.com>

SHELL ["/bin/bash", "-c"]
# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

WORKDIR /root
RUN apt-get update && \
  apt-get install -y --no-install-recommends locales curl tmux htop unzip zip git vim && \
  locale-gen en_US.UTF-8 && \
  apt-get dist-upgrade -y && \
  apt-get --purge remove openjdk* && \
  echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections && \
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
  apt-get update && \
  apt-get install -y --no-install-recommends oracle-java8-installer oracle-java8-set-default && \
  apt-get clean all && \
  rm -rf /var/lib/apt/lists/* && \
  rm -r /PI && \
  rm -r /behavioral-model && \
  rm -r /p4c && \
  git clone https://github.com/opennetworkinglab/onos.git && \
  echo 'source $ONOS_ROOT/tools/dev/bash_profile' >> /root/.bashrc && \
  echo 'export ONOS_APPS=drivers.bmv2,proxyarp,lldpprovider,hostprovider,fwd' >> /root/.bashrc
WORKDIR /root/onos

ENV ONOS_ROOT /root/onos
ENV ONOS_WEB_USER onos
ENV ONOS_WEB_PASS rocks
ENV BMV2_MN_PY /root/onos/tools/dev/mininet/bmv2.py

# Ports
# 6653 - OpenFlow
# 6640 - OVSDB
# 8181 - GUI
# 8101 - ONOS CLI
# 9876 - ONOS intra-cluster communication
EXPOSE 6653 6640 8181 8101 9876

ENTRYPOINT ["/bin/sh"]
