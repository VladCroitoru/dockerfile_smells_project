#------------------------------------------------------------------------------
# Set the base image for subsequent instructions:
#------------------------------------------------------------------------------

FROM centos:7
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>

#------------------------------------------------------------------------------
# Environment variables:
#------------------------------------------------------------------------------

ENV MESOS_VERSION="0.28.1" \
    MESOS_URL="http://repos.mesosphere.io/el/7/noarch/RPMS" \
    JENKINS_PLUGINS_URL="https://updates.jenkins-ci.org/download/plugins" \
    JENKINS_VERSION="2.19" \
    JENKINS_MESOS_VERSION="0.13.0"

#------------------------------------------------------------------------------
# Update the base image:
#------------------------------------------------------------------------------

RUN rpm --import http://mirror.centos.org/centos/7/os/x86_64/RPM-GPG-KEY-CentOS-7 \
    && yum update -y && yum clean all

#------------------------------------------------------------------------------
# Install libmesos:
#------------------------------------------------------------------------------

RUN yum install -y ${MESOS_URL}/mesosphere-el-repo-7-1.noarch.rpm \
    yum-utils subversion-libs apr-util && mkdir /tmp/mesos && cd /tmp/mesos \
    && yumdownloader mesos-${MESOS_VERSION} && rpm2cpio mesos*.rpm | cpio -idm \
    && cp usr/lib/libmesos-*.so /usr/lib/ && cd /usr/lib \
    && ln -s libmesos-*.so libmesos.so && rm -rf /tmp/mesos && yum clean all

#------------------------------------------------------------------------------
# Install jenkins:
#------------------------------------------------------------------------------

RUN rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key \
    && yum install -y java-1.7.0-openjdk-headless java-1.7.0-openjdk-devel wget openssl \
    && wget -q -O /etc/yum.repos.d/jenkins.repo \
       http://pkg.jenkins-ci.org/redhat/jenkins.repo \
    && yum install -y git jenkins-${JENKINS_VERSION} && yum clean all

#------------------------------------------------------------------------------
# Install plugins:
#------------------------------------------------------------------------------

RUN mkdir -p /var/lib/jenkins/plugins && cd /var/lib/jenkins/plugins \
    && wget -q http://updates.jenkins-ci.org/download/plugins/credentials/2.0.7/credentials.hpi \
    && wget -q http://updates.jenkins-ci.org/download/plugins/junit/1.13/junit.hpi \
    && wget -q http://updates.jenkins-ci.org/download/plugins/jackson2-api/2.7.3/jackson2-api.hpi \
    && wget -q http://updates.jenkins-ci.org/download/plugins/metrics/3.1.2.7/metrics.hpi \
    && wget -q ${JENKINS_PLUGINS_URL}/mesos/${JENKINS_MESOS_VERSION}/mesos.hpi

#------------------------------------------------------------------------------
# Populate root file system:
#------------------------------------------------------------------------------

ADD rootfs /
RUN mv /var/lib/jenkins /var/lib/jenkins_staging

#------------------------------------------------------------------------------
# Expose ports and entrypoint:
#------------------------------------------------------------------------------

ENTRYPOINT ["/init"]
