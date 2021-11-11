#################################################################
# Dockerfile
#
# Version:          1
# Software:         GRIDSS and its dependencies
# Description:      GRIDSS with java and bwa aligner
# Website:          https://github.com/lnonell/GRIDSSTest|https://hub.docker.com/r/lnonell/gridsstest
# Tags:             None, for the moment
# Base Image:       openjdk:8-jdk
# Build Cmd:        docker build biodckr/bwa 0.7.15/.CHANGE
# Pull Cmd:         docker pull biodckr/bwa CHANGE
# Run Cmd:          docker run biodckr/bwa CHANGE
#################################################################

FROM openjdk:8-jdk

#OPTIMAL WOULD BE TO COMBINE IMAGES USING ALSO THE biodckr/bwa
#APPARENTLY IMAGES CANNOT BE MERGED UNLESS

#copy-paste from https://hub.docker.com/r/biodckr/biodocker/~/dockerfile/
# Set noninterative mode
ENV DEBIAN_FRONTEND noninteractive

################## BEGIN INSTALLATION ######################

# add apt mirror
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bkp && \
#    bash -c 'echo -e "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main restricted universe multiverse\n\
#deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse\n\
#deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-backports main restricted universe multiverse\n\
#deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted universe multiverse\n\n" > /etc/apt/sources.list' && \
#    cat /etc/apt/sources.list.bkp >> /etc/apt/sources.list && \
#    cat /etc/apt/sources.list

# apt update and install global requirements
RUN apt-get clean all && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  \
        autotools-dev   \
        automake        \
        cmake           \
        curl            \
        grep            \
        sed             \
        dpkg            \
        fuse            \
        git             \
        wget            \
        zip             \
        openjdk-8-jre   \
        build-essential \
        pkg-config      \
        python          \
	python-dev      \
        python-pip      \
        bzip2           \
        ca-certificates \
        libglib2.0-0    \
        libxext6        \
        libsm6          \
        libxrender1     \
        mercurial       \
        subversion      \
        zlib1g-dev &&   \
        apt-get clean && \
        apt-get purge && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

# create shared folders
RUN mkdir /data /config

# Add user biodocker with password biodocker
RUN groupadd fuse && \
    useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse biodocker && \
    echo `echo "biodocker\nbiodocker\n" | passwd biodocker` && \
    chown biodocker:biodocker /data && \
    chown biodocker:biodocker /config

# give write permissions to conda folder
RUN chmod 777 -R /opt/conda/

# Change user
USER biodocker

# Add $HOME/bin to path
ENV PATH=$PATH:/opt/conda/bin
ENV PATH=$PATH:/home/biodocker/bin
ENV HOME=/home/biodocker

# Create $HOME/bin folder
RUN mkdir /home/biodocker/bin

# Add R and bioconda channel
RUN conda config --add channels r
RUN conda config --add channels bioconda

RUN conda upgrade conda

# Share default volumes
VOLUME ["/data", "/config"]

# Overwrite this with 'CMD []' in a dependent Dockerfile
CMD ["/bin/bash"]

#THESE LAST TWO INSTRUCTIONS ARE ALSO COMMON IN THE INSTALLATION OF BWA SO I JUST COMMENT THEMS
# change workdir
#WORKDIR /data

##################### INSTALL BWA #################
RUN conda install bwa=0.7.15

# Define default command
CMD ["bwa"]
# Change workdir to /data/
WORKDIR /data/


##################### INSTALLATION END #####################

# File Author / Maintainer
MAINTAINER Lara Nonell <lnonell@imim.es>
# Modified by Lara Nonell 11-04-2017
# Based on the combined images of biodckr/bwa, mantained by Saulo Alves Aflitos
