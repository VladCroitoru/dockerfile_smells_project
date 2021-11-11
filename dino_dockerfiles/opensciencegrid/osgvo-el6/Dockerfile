FROM centos:6

LABEL opensciencegrid.name="EL 6"
LABEL opensciencegrid.description="Enterprise Linux (CentOS) 6 base image"
LABEL opensciencegrid.url="https://www.centos.org/"
LABEL opensciencegrid.category="Base"
LABEL opensciencegrid.definition_url="https://github.com/opensciencegrid/osgvo-el6"

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
           libicu \
           libXpm \
           libXpm-devel \
           libXt \
           mesa-libGL-devel \
           numpy \
           octave \
           octave-devel \
           openssh \
           openssh-server \
           openssl098e \
           osg-wn-client \
           p7zip p7zip-plugins \
           python-astropy \
           python-devel \
           R-devel \
           redhat-lsb-core \
           rsync \
           scipy \
           stashcache-client \
           subversion \
           tcl-devel \
           tcsh \
           time \
           tk-devel \
           wget \
           which
    
# Cuda and cudnn - in case we land on GPU nodes. See:
#  https://developer.nvidia.com/cuda-downloads
#  https://gitlab.com/nvidia/cuda/blob/centos7/9.0/devel/cudnn7/Dockerfile
RUN rpm -Uvh https://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/cuda-repo-rhel6-9.0.176-1.x86_64.rpm \
    && yum -y clean all \
    && yum -y install cuda-9-1 \
    && cd /usr/local \
    && curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.1-linux-x64-v7.tgz -O \
    && tar --no-same-owner -xzf cudnn-9.1-linux-x64-v7.tgz -C /usr/local \
    && rm -f cudnn-9.1-linux-x64-v7.tgz \
    && ldconfig

# osg
RUN yum -y install osg-ca-certs osg-wn-client \
    && rm -f /etc/grid-security/certificates/*.r0

# htcondor - include so we can chirp
RUN yum -y install condor

# pegasus
RUN yum -y install pegasus

# Cleaning caches to reduce size of image
RUN yum clean all

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
        /spt \
        /stash2 \
    ; do \
        mkdir -p $MNTPOINT ; \
    done

# make OpenCL work
RUN mkdir -p /etc/OpenCL/vendors

# some extra singularity stuff
COPY .singularity.d /.singularity.d

RUN ls -la /.singularity.d/

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

