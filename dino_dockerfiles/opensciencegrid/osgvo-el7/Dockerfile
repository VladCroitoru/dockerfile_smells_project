FROM centos:7

LABEL opensciencegrid.name="EL 7"
LABEL opensciencegrid.description="Enterprise Linux (CentOS) 7 base image"
LABEL opensciencegrid.url="https://www.centos.org/"
LABEL opensciencegrid.category="Base"
LABEL opensciencegrid.definition_url="https://github.com/opensciencegrid/osgvo-el7"

RUN yum -y upgrade && \
    yum -y install epel-release yum-plugin-priorities && \
    yum -y install http://repo.opensciencegrid.org/osg/3.5/osg-3.5-el7-release-latest.rpm && \
    echo -e "# Pegasus\n[Pegasus]\nname=Pegasus\nbaseurl=http://download.pegasus.isi.edu/wms/download/rhel/7/\$basearch/\ngpgcheck=0\nenabled=1\npriority=50" >/etc/yum.repos.d/pegasus.repo && \
    yum -y groups mark convert && \
    yum -y grouplist &&\
    yum -y groupinstall "Compatibility Libraries" \
                        "Development Tools" \
                        "Scientific Support" && \
    yum -y install \
           astropy-tools \
           bc \
           binutils \
           binutils-devel \
           cmake \
           compat-glibc \
           condor \
           coreutils \
           curl \
           davix-devel \
           dcap-devel \
           doxygen \
           dpm-devel \
           fontconfig \
           gcc \
           gcc-c++ \
           gcc-gfortran \
           git \
           glew-devel \
           glib2-devel \
           glib-devel \
           globus-gass-copy-devel \
           graphviz \
           gsl-devel \
           gtest-devel \
           java-1.8.0-openjdk \
           java-1.8.0-openjdk-devel \
           json-c-devel \
           lfc-devel \
           libattr-devel \
           libgfortran \
           libGLU \
           libgomp \
           libicu \
           libquadmath \
           libssh2-devel \
           libtool \
           libtool-ltdl \
           libtool-ltdl-devel \
           libuuid-devel \
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
           nano \
           numpy \
           octave \
           octave-devel \
           openldap-devel \
           openssh \
           openssh-server \
           openssl098e \
           osg-ca-certs \
           osg-wn-client \
           p7zip \
           p7zip-plugins \
           pegasus \
           python3 \
           python36-PyYAML \
           python3-devel \
           python3-pip \
           python-astropy \
           python-devel \
           R-devel \
           redhat-lsb \
           redhat-lsb-core \
           rsync \
           scipy \
           srm-ifce-devel \
           stashcache-client \
           subversion \
           tcl-devel \
           tcsh \
           time \
           tk-devel \
           vim \
           wget \
           which \
           xrootd-client-devel \
           zlib-devel \
           && \
    rm -f /etc/grid-security/certificates/*.r0 && \
    yum clean all

# required directories
RUN for MNTPOINT in \
        /cvmfs \
        /ceph \
        /hadoop \
        /hdfs \
        /lizard \
        /mnt/hadoop \
        /mnt/hdfs \
        /xenon \
        /scratch \
        /spt \
        /stash2 \
    ; do \
        mkdir -p $MNTPOINT ; \
    done

# make sure we have a way to bind host provided libraries
# see https://github.com/singularityware/singularity/issues/611
RUN mkdir -p /host-libs /etc/OpenCL/vendors

# some extra singularity stuff
COPY .singularity.d /.singularity.d

# build info
RUN echo "Timestamp:" `date --utc` |  tee /image-build-info.txt


