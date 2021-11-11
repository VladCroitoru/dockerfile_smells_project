# Docker image for MUST week, ICS MU
FROM centos:centos7
MAINTAINER Radim Pesa

# Install software
RUN yum -y update; yum clean all
RUN yum -y install curl git make m4 wget which
RUN yum install -y gcc gcc-c++ ruby-devel openssl-devel ruby rubygems

# Install VOMS
RUN yum -y install http://repository.egi.eu/sw/production/umd/3/sl6/x86_64/updates/umd-release-3.0.1-1.el6.noarch.rpm
RUN curl -s http://repository.egi.eu/community/software/rocci.cli/4.3.x/releases/repofiles/sl-6-x86_64.repo > /etc/yum.repos.d/rocci.repo
RUN yum -q -y install ca-policy-egi-core fetch-crl voms-clients

# Create VOMS directories and copy files
RUN mkdir -p /etc/grid-security/vomsdir/fedcloud.egi.eu
COPY vomses /etc/vomses
COPY voms1.grid.cesnet.cz.lsc /etc/grid-security/vomsdir/fedcloud.egi.eu
COPY voms2.grid.cesnet.cz.lsc /etc/grid-security/vomsdir/fedcloud.egi.eu

# Install OCCI-CLI
RUN gem install occi-cli
ENV PATH /usr/loca/bin:$PATH

# Install Cloudify 
RUN yum install -y python-virtualenv python-pip
RUN wget -O get-cloudify.py 'http://repository.cloudifysource.org/org/cloudify3/get-cloudify.py'
RUN python get-cloudify.py -e ~/cfy
RUN unlink get-cloudify.py

WORKDIR /root
CMD ["/bin/bash"]

