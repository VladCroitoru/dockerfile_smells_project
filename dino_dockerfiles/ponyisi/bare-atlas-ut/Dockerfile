## University of Texas - Austin configuration
## Condor and local squid - no autodiscovery

FROM hepsw/slc-base
MAINTAINER Peter Onyisi "ponyisi@cern.ch"

# Frontier configuration
ENV ALRB_localConfigDir /root/localConfig

# install HEP base libraries
# Install Condor
ADD etc-yum-htcondor.repo /etc/yum.repos.d/htcondor-stable.repo
ADD condor_config.local /etc/condor/condor_config.local

# Install OSG WN base
# Install ganglia
RUN yum -y install http://linuxsoft.cern.ch/cern/slc64/x86_64/yum/extras/HEP_OSlibs_SL6-1.0.16-0.el6.x86_64.rpm condor yum-plugin-priorities https://repo.grid.iu.edu/osg/3.3/osg-3.3-el6-release-latest.rpm osg-wn-client wget rsync nano sudo ganglia-gmond fuse fuse-libs ; yum clean all
ADD etc-ganglia-gmond.conf /etc/ganglia/gmond.conf

#ADD etc-cvmfs-default-local /etc/cvmfs/default.local
ADD localFrontierSquid.sh /root/localConfig/localFrontierSquid.sh

ADD setup-cvmfs-portable.sh /etc/cvmfs/setup-cvmfs-portable.sh
ADD startcondor.sh /root/startcondor.sh
#ADD etc-cubied-condor.conf /etc/cubie.d/condor.conf
ADD start.sh /root/start.sh
ADD etc-fuse.conf /etc/fuse.conf

RUN chmod uga+rx /etc/cvmfs/setup-cvmfs-portable.sh /root/startcondor.sh /root/start.sh
RUN usermod -a -G fuse nobody

ENTRYPOINT /root/start.sh
