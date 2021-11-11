FROM quay.io/kbase/centos:7
ENV container docker

# These ARGs values are passed in via the docker build command
ARG BUILD_DATE
ARG VCS_REF
ARG BRANCH=develop


# Get commonly used utilities
RUN yum -y update && yum update -y systemd && yum -y install -y epel-release wget which git deltarpm gcc libcgroup libcgroup-tools stress-ng

# Install docker binaries 
RUN yum install -y yum-utils device-mapper-persistent-data lvm2 && yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && yum install -y docker-ce

# Install DOCKERIZE
RUN curl -o /tmp/dockerize.tgz https://raw.githubusercontent.com/kbase/dockerize/dist/dockerize-linux-amd64-v0.5.0.tar.gz && \
      cd /usr/bin && \
      tar xvzf /tmp/dockerize.tgz && \
      rm /tmp/dockerize.tgz

# Install HTCondor
RUN cd /etc/yum.repos.d && \
      wget http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-development-rhel7.repo && \
      wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor && \
      rpm --import RPM-GPG-KEY-HTCondor && yum -y install condor

#ADD DIRS
RUN mkdir -p /var/run/condor && mkdir -p /var/log/condor && mkdir -p /var/lock/condor && mkdir -p /var/lib/condor/execute


COPY deployment/conf /etc/condor/
COPY deployment/bin/start-condor.sh /usr/sbin/start-condor.sh

RUN adduser condor_pool

RUN mkdir -p /usr/local/condor/run/condor /usr/local/condor/log/condor /usr/local/condor/lock/condor /usr/local/condor/lib/condor/spool /usr/local/condor/lib/condor/execute


# The BUILD_DATE value seem to bust the docker cache when the timestamp changes, move to
# the end
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/kbase/condor.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1" \
      us.kbase.vcs-branch=$BRANCH \
      maintainer="Steve Chan sychan@lbl.gov"

ENTRYPOINT [ "/usr/bin/dockerize" ]
CMD [ "-template", "/etc/condor/.templates/condor_config.local.templ:/etc/condor/condor_config.local", \
      "-stdout", "/var/log/condor/SchedLog", \
      "/usr/sbin/start-condor.sh" ]
