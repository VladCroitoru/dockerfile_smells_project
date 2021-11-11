FROM pnnlhep/osg-compute-stable
MAINTAINER Malachi Schram "malachi.schram@pnnl.gov"

## Problem with /tmp permission (?)
RUN chmod 777 -R /tmp

### INSTALL PACKAGES
RUN yum install -y fuse cvmfs cvmfs-config-osg; echo user_allow_other > /etc/fuse.conf
ADD ./startCVMFS.sh /etc/startCVMFS.sh
RUN chmod +x /etc/startCVMFS.sh
RUN export REPO=belle.cern.ch; /etc/startCVMFS.sh
#
## INSTALL PACKAGES
#RUN yum install -y fuse cvmfs cvmfs-config-osg; echo user_allow_other > /etc/fuse.conf

## Setup AUTOFS
#RUN echo "/cvmfs /etc/auto.cvmfs" >> /etc/auto.master
#RUN service autofs restart

## Setup CVMFS
#RUN cvmfs_config setup
#RUN echo 'CVMFS_REPOSITORIES="belle.cern.ch"' >> /etc/cvmfs/default.local 
#RUN cvmfs_config probe
#RUN ls /cvmfs/belle.cern.ch || true


## OSG CVMFS instructions
#
## CERN CVMFS instructions
#RUN yum -y install cvmfs cvmfs-config-default
#RUN cvmfs_config setup
#RUN echo 'CVMFS_REPOSITORIES="belle.cern.ch"' >> /etc/cvmfs/default.local 
#RUN cvmfs_config probe
#RUN service autofs restart

## Copy Belle II tools
RUN mkdir -p /tmp/cvmfs/belle.cern.ch/sl6/
RUN cd /tmp/cvmfs/belle.cern.ch/sl6/
RUN rsync -lr /cvmfs/belle.cern.ch/sl6/tools ./ 

## Copy Belle II externals
RUN mkdir -p /tmp/cvmfs/belle.cern.ch/sl6/externals
RUN cd /tmp/cvmfs/belle.cern.ch/sl6/externals
RUN rsync -lr /cvmfs/belle.cern.ch/sl6/externals/v01-01-08 ./

## Copy Belle II prod release
RUN mkdir -p /tmp/cvmfs/belle.cern.ch/sl6/releases
RUN cd /tmp/cvmfs/belle.cern.ch/sl6/releases
RUN rsync -lr /cvmfs/belle.cern.ch/sl6/releases/release-00-07-01 ./

## Stop CVMFS and copy hard version
RUN service autofs stop
RUN ls /cvmfs/belle.cern.ch
RUN mkdir -p /cvmfs/belle.cern.ch
RUN mv /tmp/cvmfs/belle.cern.ch/sl6 /cvmfs/belle.cern.ch/sl6

## Not sure I need this anymore
ADD ./start.sh /etc/start.sh
RUN chmod +x /etc/start.sh

CMD ["/etc/start.sh"]
