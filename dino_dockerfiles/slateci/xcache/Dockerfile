FROM centos:7

LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>

# ENV XCVERSION=5.0.0-1.el7
ENV XCVERSION=5.0.0-1.1.osgup.el7

RUN yum -y update

# gperftools - for tcmalloc
RUN yum install -y \
    gperftools \
    curl \
    hostname   

RUN yum install -y https://repo.opensciencegrid.org/osg/3.5/osg-3.5-el7-release-latest.rpm; \
    yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm;

RUN curl -s -o /etc/pki/rpm-gpg/RPM-GPG-KEY-wlcg http://linuxsoft.cern.ch/wlcg/RPM-GPG-KEY-wlcg; \
    curl -s -o /etc/yum.repos.d/wlcg-centos7.repo http://linuxsoft.cern.ch/wlcg/wlcg-centos7.repo; \
    curl -s -L -o /etc/yum.repos.d/xrootd-stable-slc7.repo http://www.xrootd.org/binaries/xrootd-stable-slc7.repo


RUN yum install -y xrootd-server-$XCVERSION xrootd-client-$XCVERSION xrootd-$XCVERSION \
    xrootd-voms-$XCVERSION voms-clients wlcg-voms-atlas fetch-crl osg-ca-certs

RUN yum localinstall -y https://repo.opensciencegrid.org/osg/upcoming/el7/development/x86_64/xrootd-rucioN2N-for-Xcache-1.2-3.3.osgup.el7.x86_64.rpm


RUN yum install -y \
    python-pip \
    python36 \
    gcc \
    python3-devel \
    jq

RUN pip install --upgrade pip requests

# python3
# RUN python3 -m ensurepip
RUN pip3 install --upgrade pip requests wheel psutil

# adding user group atlas access rights (read and list)
RUN echo "g /atlas / rl" > /etc/xrootd/auth_db; \
    touch /etc/xrootd/xcache.cfg /var/run/x509up

# not sure this line is needed
RUN mkdir -p /xrd/var/log /xrd/var/spool /xrd/var/run /tests

COPY xcache_limits.conf /etc/security/limits.d
COPY xcache.cfg /etc/xrootd/
COPY runme.sh run_cache_reporter.sh run_x509_updater.sh updateAGISstatus.sh updateCRICstatus.sh /
COPY cacheReporter/*.py /
COPY tests/* /tests/

# xrootd user is created during installation
# here we will fix its GID and UID so files created by one container will be modifiable by the next.
RUN groupmod -o -g 10940 xrootd
RUN usermod -o -u 10940 -g 10940 -s /bin/sh xrootd

# not sure the two lines bellow are needed at all
# if needed change ownership of directories
RUN if [ $(stat -c "%U:%G" /xrd/var ) != "xrootd:xrootd" ]; then chown -R xrootd:xrootd /xrd/var; fi
RUN if [ $(stat -c "%U:%G" /xrd ) != "xrootd:xrootd" ]; then chown -R xrootd:xrootd /xrd; fi

# build  
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

CMD [ "/runme.sh" ]
