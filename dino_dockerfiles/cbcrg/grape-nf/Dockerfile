FROM ubuntu:precise

MAINTAINER Paolo Di Tommaso <paolo.ditommaso@gmail.com>

#
# Install pre-requistes
#
RUN apt-get update -q --fix-missing; \
  apt-get install -q -y openjdk-7-jre-headless wget curl unzip; 

# Samtools + Cufflinks 
RUN apt-get install -q -y samtools libboost-all-dev 

# Cufflinks
RUN wget -q http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.1.1.Linux_x86_64.tar.gz && \
  tar xf cufflinks-2.1.1.Linux_x86_64.tar.gz -C /opt && \
  rm -rf cufflinks-2.1.1.Linux_x86_64.tar.gz && \
  ln -s /opt/cufflinks-2.1.1.Linux_x86_64/ /opt/cufflinks

# GEMtools
RUN wget -q http://barnaserver.com/gemtools/releases/GEMTools-static-core2-1.7.1.tar.gz && \
  tar xf GEMTools-static-core2-1.7.1.tar.gz -C /opt && \
  rm -rf GEMTools-static-core2-1.7.1.tar.gz && \
  ln -s /opt/gemtools-1.7.1-core2 /opt/gemtools  

# Flux Capacitor
RUN wget -q http://artifactory.sammeth.net/artifactory/barna/barna/barna.capacitor/1.2.4/flux-capacitor-1.2.4.tgz && \
  tar xf flux-capacitor-1.2.4.tgz -C /opt && \
  rm -rf flux-capacitor-1.2.4.tgz && \
  ln -s /opt/flux-capacitor-1.2.4 /opt/flux
 
# Bowtie 
RUN wget -q -O bowtie2-2.2.1-linux-x86_64.zip \
  'http://downloads.sourceforge.net/project/bowtie-bio/bowtie2/2.2.1/bowtie2-2.2.1-linux-x86_64.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fbowtie-bio%2Ffiles%2Fbowtie2%2F2.2.1%2F&ts=1395738113&use_mirror=freefr' && \
  unzip -q bowtie2-2.2.1-linux-x86_64.zip -d /opt && \
  rm -rf bowtie2-2.2.1-linux-x86_64.zip && \
  ln -s /opt/bowtie2-2.2.1 /opt/bowtie2
  
# Install tophat2
RUN  wget -q http://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.13.Linux_x86_64.tar.gz && \
 tar xf tophat-2.0.13.Linux_x86_64.tar.gz -C /opt && \
 rm -rf tophat-2.0.13.Linux_x86_64.tar.gz && \
 ln -s /opt/tophat-2.0.13.Linux_x86_64 /opt/tophat2
 
  
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/cufflinks:/opt/gemtools/bin:/opt/flux/bin:/opt/bowtie2:/opt/tophat2
