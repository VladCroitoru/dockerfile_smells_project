###########################################################
# Dockerfile to build STAR container images
# Based on Ubuntu
############################################################
#Build the image based on Ubuntu
FROM ubuntu:latest

#Maintainer and author
MAINTAINER Magdalena Arnal <marnal@imim.es>

#Install required packages in ubuntu for STAR
RUN apt-get update
RUN apt-get install --yes build-essential gcc-multilib apt-utils zlib1g-dev git

#Install STAR
WORKDIR /usr/local/
RUN git clone https://github.com/alexdobin/STAR.git
WORKDIR /usr/local/STAR/
RUN git checkout 2.6.1b
WORKDIR /usr/local/STAR/source
RUN make STAR
ENV PATH /usr/local/STAR/source:$PATH

#Install required libraries in ubuntu for samtools
RUN apt-get update -y && apt-get install -y \
    wget unzip bzip2 g++ make ncurses-dev python default-jdk default-jre libncurses5-dev \
    libbz2-dev liblzma-dev
#Set wokingDir in /bin
WORKDIR /bin

#Install and Configure samtools
RUN wget http://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
RUN tar --bzip2 -xf samtools-1.5.tar.bz2
WORKDIR /bin/samtools-1.5
RUN ./configure
RUN make
RUN rm /bin/samtools-1.5.tar.bz2
ENV PATH $PATH:/bin/samtools-1.5

# Clean up and set Workingdir at Home
RUN apt-get clean
RUN apt-get remove --yes --purge build-essential gcc-multilib apt-utils zlib1g-dev wget
WORKDIR /
