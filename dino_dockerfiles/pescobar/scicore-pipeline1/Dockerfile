FROM centos:7.3.1611
MAINTAINER Pablo Escobar <pablo.escobarlopez@unibas.ch>

ENV STAR_VERSION=2.5.2b
ENV HTSEQ_VERSION=0.6.1p1
ENV PYSAM_VERSION=0.9.0

# install the build dependencies
RUN yum makecache fast && \
    yum -y install epel-release && \
    yum -y install \
    make \
    gcc \
    gcc-c++ \
    zlib-devel \
    python-devel \
    python-pip \
    numpy \
 && yum clean all

# Download STAR sources tarball
WORKDIR /usr/local/src
RUN curl -o STAR-${STAR_VERSION}.tar.gz https://codeload.github.com/alexdobin/STAR/tar.gz/${STAR_VERSION} && \
    mkdir STAR-${STAR_VERSION}-src && \
    tar --extract --file STAR-${STAR_VERSION}.tar.gz --directory STAR-${STAR_VERSION}-src --strip-components=1

# compile STAR and STARlong binaries and copy them to /usr/local/bin
WORKDIR /usr/local/src/STAR-${STAR_VERSION}-src/source
RUN make STAR && \
    cp STAR /usr/local/bin/
RUN make STARlong && \
    cp STARlong /usr/local/bin/

# Install HTSeq
RUN pip install HTSeq==${HTSEQ_VERSION}

# Install Pysam
RUN pip install Pysam==${PYSAM_VERSION}

ENTRYPOINT ["echo", "-e", "This container includes the following apps:\\n\
    STAR version ${STAR_VERSION} - https://github.com/alexdobin/STAR\\n\
    HTSeq version ${HTSEQ_VERSION} - http://www-huber.embl.de/HTSeq/\\n\
    Pysam version ${PYSAM_VERSION} - https://github.com/pysam-developers/pysam\\n\
    To execute a binary inside the container do \"singularity exec /path/to/container.img binary-name\""]
