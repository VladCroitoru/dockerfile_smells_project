# Lastest ubuntu:trusty
FROM ubuntu:trusty

MAINTAINER Patrik Hagedorn <p.hagedorn@visono.com>

USER root

WORKDIR /

# OpenVSwitch version
ENV OVS_VERSION="openvswitch-2.3.2"

# Install build dependencies
RUN apt-get update \
&& apt-get install -y \
    build-essential \
    fakeroot \
    debhelper \
    autoconf \
    automake \
    bzip2 \
    libssl-dev \
    openssl \
    graphviz \
    python-all \
    procps \
    python-qt4 \
    python-zopeinterface \
    python-twisted-conch \
    libtool \
    wget \
&& apt-get autoclean -y \
&& apt-get autoremove -y

# Fetch the latest archive and build without check in parallel
RUN wget http://openvswitch.org/releases/${OVS_VERSION}.tar.gz \
&& tar xzvf ${OVS_VERSION}.tar.gz \
&& rm ${OVS_VERSION}.tar.gz \
&& cd ${OVS_VERSION} && DEB_BUILD_OPTIONS='parallel=8 nocheck' fakeroot debian/rules binary \
&& mkdir /${OVS_VERSION}-build

# Adding scripts
COPY run.sh /run.sh
RUN chmod 755 /*.sh

CMD ["/run.sh"]