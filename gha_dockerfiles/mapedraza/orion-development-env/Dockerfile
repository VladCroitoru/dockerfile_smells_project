# Copyright 2020 Telefonica Investigacion y Desarrollo, S.A.U
#
# This file is part of Orion Context Broker.
#
# Orion Context Broker is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Orion Context Broker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Orion Context Broker. If not, see http://www.gnu.org/licenses/.
#
# For those usages not covered by this license please contact with
# iot_support at tid dot es
#

ARG  IMAGE_TAG=centos8.3.2011
FROM centos:${IMAGE_TAG}

ARG GITHUB_ACCOUNT=telefonicaid
ARG GITHUB_REPOSITORY=fiware-orion

ARG GIT_NAME
ARG GIT_REV_ORION
ARG CLEAN_DEV_TOOLS

ENV ORION_USER orion
ENV GIT_NAME ${GIT_NAME:-telefonicaid}
ENV GIT_REV_ORION ${GIT_REV_ORION:-master}
ENV CLEAN_DEV_TOOLS ${CLEAN_DEV_TOOLS:-1}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /opt

RUN \
    adduser --comment "${ORION_USER}" ${ORION_USER} && \
    # Install dependencies
    yum -y install epel-release && \
    yum -y install \
      boost-devel \
      bzip2 \
      cmake \
      gnutls-devel \
      libgcrypt-devel \
      libcurl-devel \
      openssl-devel \
      libuuid-devel \
      make \
      nc \
      git \
      gcc-c++ \
      tar \
      which \
      cyrus-sasl-devel && \
    # FIXME: this is a temporary hack due to the cmake version that comes with CentOS8
    # at the present moment (June 9th, 2021) is 3.18.2. Unfortunatelly, this version seems
    # to have problems to build the mongo C driver (see https://jira.mongodb.org/browse/CDRIVER-4020),
    # probably due to a bug already solved in 3.18.3. Thus, the solution is to build cmake
    # from scratch (we have used 3.20.1, the last version by the time being). Once CentOS8
    # upgrade cmake to a version beyond 3.18.2, we can probably remove this hack and rely again in
    # yum-based installation
    rpm -e cmake cmake-data cmake-filesystem cmake-rpm-macros && \
    cd /opt && \
    curl -OL https://github.com/Kitware/CMake/releases/download/v3.20.1/cmake-3.20.1.tar.gz && \
    tar xvf cmake-3.20.1.tar.gz && \
    cd cmake-3.20.1 && \
    ./bootstrap && \
    make && \
    make install && \
    # Install libmicrohttpd from source
    cd /opt && \
    curl -kOL http://ftp.gnu.org/gnu/libmicrohttpd/libmicrohttpd-0.9.70.tar.gz && \
    tar xvf libmicrohttpd-0.9.70.tar.gz && \
    cd libmicrohttpd-0.9.70 && \
    ./configure --disable-messages --disable-postprocessor --disable-dauth && \
    make && \
    make install && \
    ldconfig && \
    # Install mosquitto from source
    cd /opt && \
    curl -kOL http://mosquitto.org/files/source/mosquitto-2.0.12.tar.gz && \
    tar xvf mosquitto-2.0.12.tar.gz && \
    cd mosquitto-2.0.12 && \
    sed -i 's/WITH_CJSON:=yes/WITH_CJSON:=no/g' config.mk && \
    sed -i 's/WITH_STATIC_LIBRARIES:=no/WITH_STATIC_LIBRARIES:=yes/g' config.mk && \
    sed -i 's/WITH_SHARED_LIBRARIES:=yes/WITH_SHARED_LIBRARIES:=no/g' config.mk && \
    make && \
    make install && \
    ldconfig && \
    # Install mongodb driver from source
    cd /opt && \
    curl -kOL https://github.com/mongodb/mongo-c-driver/releases/download/1.17.4/mongo-c-driver-1.17.4.tar.gz && \
    tar xfvz mongo-c-driver-1.17.4.tar.gz && \
    cd mongo-c-driver-1.17.4 && \
    mkdir cmake-build && \
    cd cmake-build && \
    cmake -DENABLE_AUTOMATIC_INIT_AND_CLEANUP=OFF ..   && \
    make && \
    make install && \
    # Install rapidjson from source
    cd /opt && \
    curl -kOL https://github.com/miloyip/rapidjson/archive/v1.1.0.tar.gz && \
    tar xfz v1.1.0.tar.gz && \
    mv rapidjson-1.1.0/include/rapidjson/ /usr/local/include 
    # Install orion from source
    
WORKDIR /

# Note we disable log file as docker container will output by stdout
# ENTRYPOINT ["/usr/bin/contextBroker","-fg", "-multiservice", "-ngsiv1Autocast", "-disableFileLog" ]
ENTRYPOINT ["/bin/bash", "/opt/script/script.sh"]

EXPOSE 1026

LABEL "maintainer"="Orion Team. Telefónica I+D"
LABEL "org.opencontainers.image.authors"="iot_support@tid.es"
LABEL "org.opencontainers.image.documentation"="https://fiware-orion.rtfd.io/"
LABEL "org.opencontainers.image.vendor"="Telefónica Investigación y Desarrollo, S.A.U"
LABEL "org.opencontainers.image.licenses"="AGPL-3.0-only"
LABEL "org.opencontainers.image.title"="Orion Context Broker"
LABEL "org.opencontainers.image.description"="The Orion Context Broker is an implementation of the Publish/Subscribe Context Broker GE, providing an NGSI interface"
LABEL "org.opencontainers.image.source"=https://github.com/${GITHUB_ACCOUNT}/${GITHUB_REPOSITORY}

# Create an anonymous user
RUN sed -i -r "/^(root|nobody)/!d" /etc/passwd /etc/shadow /etc/group \
    && sed -i -r 's#^(.*):[^:]*$#\1:/sbin/nologin#' /etc/passwd
USER nobody


