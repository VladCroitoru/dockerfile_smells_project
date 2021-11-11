#################################################################
# Dockerfile
#
# Version:          1
# Software:         CoNVaDING and its dependencies
# Description:      CoNVaDING (Copy Number Variation Detection In Next-generation sequencing Gene panels)
# Website:          https://molgenis.gitbooks.io/convading/
# Tags:             None, for the moment
# Base Image:       perl:5.26
# Mantainer:        Lara Nonell
#################################################################

FROM ubuntu:14.04

# Update the repository sources list
RUN apt-get update

# Install compiler and perl stuff
RUN apt-get install --yes \
build-essential \
gcc-multilib \
apt-utils \
perl \
expat \
libexpat-dev \
wget git unzip bzip2 g++ make zlib1g-dev ncurses-dev python default-jdk default-jre libncurses5-dev \
libbz2-dev liblzma-dev

RUN apt-get install -y cpanminus
RUN cpanm --installdeps Statistics::Normality

#Install and Configure samtools
RUN wget http://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
RUN tar --bzip2 -xf samtools-1.5.tar.bz2
WORKDIR /bin/samtools-1.5
ENV PATH $PATH:/bin/samtools-1.5

WORKDIR /bin

RUN wget https://github.com/molgenis/CoNVaDING/archive/1.2.1.tar.gz
RUN tar -xf 1.2.1.tar.gz
WORKDIR /bin/CoNVaDING-1.2.1
#ENV PATH $PATH:/bin/CoNVaDING-1.2.1

#Set WorkingDir
WORKDIR /
