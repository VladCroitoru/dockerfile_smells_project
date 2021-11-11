# java include from https://github.com/ibmruntimes/ci.docker/blob/9bd29a750a39cd8f89c9dcd3a4791cf6548a5344/ibmjava/8/jre/alpine/Dockerfile
# (C) Copyright IBM Corporation 2016, 2017
#
# ------------------------------------------------------------------------------
#               NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"
#
#                       PLEASE DO NOT EDIT IT DIRECTLY.
# ------------------------------------------------------------------------------
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



FROM jenkins/jenkins:2.89.2

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

#get rid of admin password setup
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"


USER root
RUN apt-get update && apt-get install subversion locales


# add ibm java
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_VERSION 1.8.0_sr5fp6

RUN set -eux; \
    ARCH="$(dpkg --print-architecture)"; \
    case "${ARCH}" in \
       amd64|x86_64) \
         ESUM='b5e2824313e62d647c7c7c7c8a6eb8704e445e915da460d379aedd30e6835030'; \
         YML_FILE='sdk/linux/x86_64/index.yml'; \
         ;; \
       i386) \
         ESUM='5e2fd0cafeab9c72e8eb038eb22cf911a18607298a47cd3d4684179610ec364c'; \
         YML_FILE='sdk/linux/i386/index.yml'; \
         ;; \
       ppc64el|ppc64le) \
         ESUM='c2dc7e1cf3db66f7ea0497b48ecb79048a553eaa82d5595a43c9bd7542610b0b'; \
         YML_FILE='sdk/linux/ppc64le/index.yml'; \
         ;; \
       s390) \
         ESUM='5f3f12fefe36502954d69fb1178c2a8bcd88624bc77c4c7bafd9193adcc79398'; \
         YML_FILE='sdk/linux/s390/index.yml'; \
         ;; \
       s390x) \
         ESUM='116fbee3c36425056d6310dd6ef54ce3debdd7150fa57e28caf39f04108b3edc'; \
         YML_FILE='sdk/linux/s390x/index.yml'; \
         ;; \
       *) \
         echo "Unsupported arch: ${ARCH}"; \
         exit 1; \
         ;; \
    esac; \
    BASE_URL="https://public.dhe.ibm.com/ibmdl/export/pub/systems/cloud/runtimes/java/meta/"; \
    wget -q -U UA_IBM_JAVA_Docker -O /tmp/index.yml ${BASE_URL}/${YML_FILE}; \
    JAVA_URL=$(cat /tmp/index.yml | sed -n '/'${JAVA_VERSION}'/{n;p}' | sed -n 's/\s*uri:\s//p' | tr -d '\r'); \
    wget -q -U UA_IBM_JAVA_Docker -O /tmp/ibm-java.bin ${JAVA_URL}; \
    echo "${ESUM}  /tmp/ibm-java.bin" | sha256sum -c -; \
    echo "INSTALLER_UI=silent" > /tmp/response.properties; \
    echo "USER_INSTALL_DIR=/opt/ibm/java" >> /tmp/response.properties; \
    echo "LICENSE_ACCEPTED=TRUE" >> /tmp/response.properties; \
    mkdir -p /opt/ibm; \
    chmod +x /tmp/ibm-java.bin; \
    /tmp/ibm-java.bin -i silent -f /tmp/response.properties; \
    rm -f /tmp/response.properties; \
    rm -f /tmp/index.yml; \
    rm -f /tmp/ibm-java.bin; \
    cd /opt/ibm/java/jre/lib; \
    rm -rf icc;
    
    
#end add ibm java

#RUN locale-gen en_US.UTF-8  
#ENV LANG en_US.UTF-8  
#ENV LANGUAGE en_US:en  
#ENV LC_ALL en_US.UTF-8  


#RUN locale-gen de_DE.UTF-8  
#ENV LANG de_DE.UTF-8  
#ENV LANGUAGE de_DE:de  
#ENV LC_ALL de_DE.UTF-8  
#RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

#RUN export LANGUAGE=de_DE.UTF-8; export LANG=de_DE.UTF-8; export LC_ALL=de_DE.UTF-8; locale-gen de_DE.UTF-8; DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales


RUN sed -i -e 's/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=de_DE.UTF-8
ENV LANG de_DE.UTF-8

# ENTRYPOINT cp /var/share/jenkins_ssh_key/id_rsa /root/.ssh/id_rsa && chmod 0600 /root/.ssh/id_rsa
