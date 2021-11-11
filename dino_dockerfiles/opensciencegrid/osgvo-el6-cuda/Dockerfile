from nvidia/cuda:8.0-cudnn6-devel-centos6
MAINTAINER Edgar Fajardo "emfajard@ucsd.edu"

ADD environment /environment
ADD exec        /.exec
ADD run         /.run
ADD shell       /.shell

RUN chmod 755 .exec .run .shell

RUN yum -y upgrade
RUN yum -y install epel-release yum-plugin-priorities

# osg repo
RUN yum -y install http://repo.opensciencegrid.org/osg/3.4/osg-3.4-el6-release-latest.rpm
   
# pegasus repo 
RUN echo -e "# Pegasus\n[Pegasus]\nname=Pegasus\nbaseurl=http://download.pegasus.isi.edu/wms/download/rhel/6/\$basearch/\ngpgcheck=0\nenabled=1\npriority=50" >/etc/yum.repos.d/pegasus.repo

# well rounded basic system to support a wide range of user jobs
RUN yum -y grouplist \
    && yum -y groupinstall "Additional Development" \
                           "Compatibility Libraries" \
                           "Console Internet Tools" \
                           "Development Tools" \
                           "Internet Applications" \
                           "Networking Tools" \
                           "Scientific Support"

RUN yum -y install \
           redhat-lsb \
           astropy-tools \
           bc \
           binutils \
           binutils-devel \
           coreutils \
           curl \
           fontconfig \
           gcc \
           gcc-c++ \
           gcc-gfortran \
           git \
           glew-devel \
           glib2-devel \
           glib-devel \
           graphviz \
           gsl-devel \
           java-1.8.0-openjdk \
           java-1.8.0-openjdk-devel \
           libgfortran \
           libGLU \
           libX11-devel \
           libXaw-devel \
           libXext-devel \
           libXft-devel \
           libxml2 \
           libxml2-devel \
           libXmu-devel \
           libXpm \
           libXpm-devel \
           libXt \
           mesa-libGL-devel \
           numpy \
           octave \
           octave-devel \
           openssl098e \
	   osg-wn-client \
           p7zip p7zip-plugins \
           python-astropy \
           python-devel \
           R-devel \
           redhat-lsb-core \
           rsync \
           scipy \
           subversion \
           tcl-devel \
           tcsh \
           time \
           tk-devel \
           wget \
           which \
    
# osg
# use CA certs from CVMFS
RUN yum -y install osg-ca-certs osg-wn-client \
    && mv /etc/grid-security/certificates /etc/grid-security/certificates.osg-ca-certs \
    && ln -f -s /cvmfs/oasis.opensciencegrid.org/mis/certificates /etc/grid-security/certificates

# htcondor - include so we can chirp
RUN yum -y install condor

# pegasus
RUN yum -y install pegasus

# required directories
RUN mkdir -p /cvmfs
RUN mkdir -p /etc/OpenCL/vendors

# verification
RUN ls -l /etc/grid-security/

# make sure we have a way to bind host provided libraries
# see https://github.com/singularityware/singularity/issues/611
RUN mkdir -p /host-libs && \
    echo "/host-libs/" >/etc/ld.so.conf.d/000-host-libs.conf

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

