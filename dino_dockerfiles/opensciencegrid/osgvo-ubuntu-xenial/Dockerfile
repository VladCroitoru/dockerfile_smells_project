FROM ubuntu:xenial

LABEL opensciencegrid.name="Ubuntu 16.04"
LABEL opensciencegrid.description="Ubuntu 16.04 (Xenial) base image"
LABEL opensciencegrid.url="https://www.ubuntu.com"
LABEL opensciencegrid.category="Base"
LABEL opensciencegrid.definition_url="https://github.com/opensciencegrid/osgvo-ubuntu-xenial"

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        curl \
        davix-dev \
        dcap-dev \
        fonts-freefont-ttf \
        g++ \
        gcc \
        gfal2 \
        gfortran \
        git \
        libafterimage-dev \
        libavahi-compat-libdnssd-dev \
        libcfitsio-dev \
        libfftw3-dev \
        libfreetype6-dev \
        libfreetype6-dev \
        libftgl-dev \
        libgfal2-dev \
        libgif-dev \
        libgl2ps-dev \
        libglew-dev \
        libglu-dev \
        libgraphviz-dev \
        libgsl-dev \
        libjemalloc-dev \
        libjpeg-dev \
        libkrb5-dev \
        libldap2-dev \
        liblz4-dev \
        liblzma-dev \
        libmysqlclient-dev \
        libpcre++-dev \
        libpng12-dev \
        libpng-dev \
        libpq-dev \
        libpythia8-dev \
        libqt4-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libtbb-dev \
        libtiff-dev \
        libx11-dev \
        libxext-dev \
        libxft-dev \
        libxml2-dev \
        libxpm-dev \
        libz-dev \
        libzmq3-dev \
        locales \
        lsb-release \
        make \
        module-init-tools \
        openjdk-8-jdk \
        pkg-config \
        python \
        python3 \
        python3-pip \
        python3-tk \
        python-dev \
        python-numpy \
        python-pip \
        r-base \
        r-cran-rcpp \
        r-cran-rinside \
        rsync \
        srm-ifce-dev \
        unixodbc-dev \
        unzip \
        vim \
        wget \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# use CA certs from CVMFS
RUN mkdir -p /etc/grid-security && \
    ln -f -s /cvmfs/oasis.opensciencegrid.org/mis/certificates /etc/grid-security/certificates

# stashcp
RUN pip install --upgrade pip==9.0.3 && \
    pip install setuptools && \
    pip install stashcp

# required directories
RUN for MNTPOINT in \
        /cvmfs \
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

# make sure we have a way to bind host provided libraries
# see https://github.com/singularityware/singularity/issues/611
RUN mkdir -p /host-libs /etc/OpenCL/vendors

# some extra singularity stuff
COPY .singularity.d /.singularity.d

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

