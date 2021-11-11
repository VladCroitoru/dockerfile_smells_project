FROM ubuntu:xenial
MAINTAINER David Spencer <dspencer@wustl.edu>

LABEL \
    description="Haley's Walkers"

RUN apt-get update -y && apt-get install -y \
    ant \
    apt-utils \
    build-essential \
    bzip2 \
    default-jdk \
    default-jre \
    gcc-multilib \
    git \
    libncurses5-dev \
    libnss-sss \
    nodejs \
    tzdata \
    unzip \
    wget \
    zlib1g-dev \
    perl \
    expat \
    libexpat-dev

##########
#Haley's GATK 3.6#
##########
#ENV maven_package_name apache-maven-3.3.9
#RUN cd /tmp/ && wget -q http://mirror.nohup.it/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.zip

WORKDIR /opt
RUN git clone -b dev --recursive https://github.com/abelhj/gatk.git
    
#RUN cd /opt/ && unzip /tmp/${maven_package_name}-bin.zip \
#    && rm -rf /tmp/${maven_package_name}-bin.zip LICENSE NOTICE README.txt \
#    && cd /opt/ \
#    && cd /opt/gatk && /opt/${maven_package_name}/bin/mvn verify -P\!queue

ENV SAMTOOLS_INSTALL_DIR=/opt/samtools

WORKDIR /tmp
RUN wget https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2 && \
  tar --bzip2 -xf samtools-1.3.1.tar.bz2

WORKDIR /tmp/samtools-1.3.1
RUN ./configure --enable-plugins --prefix=$SAMTOOLS_INSTALL_DIR && \
  make all all-htslib && \
  make install install-htslib

WORKDIR /
RUN ln -s $SAMTOOLS_INSTALL_DIR/bin/samtools /usr/bin/samtools && \
  rm -rf /tmp/samtools-1.3.1
 
WORKDIR /opt

ADD CalculateContamination.pl /opt/


