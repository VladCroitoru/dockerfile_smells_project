#########################################################################
#RNA-seq Tools
#Dockerfile to use Cufflinks Cuffcompare Cuffmerge and Cuffdiff 2.2.1
#Ubuntu 14.04
##########################################################################
#Build the image based on Ubuntu
FROM ubuntu:14.04

#Maintainer and author
MAINTAINER Magdalena Arnal <marnal@imim.es>

#Update and install packages wget, unzip and python
RUN apt-get update -y && apt-get install -y \
    wget git unzip bzip2 g++ make zlib1g-dev ncurses-dev python default-jdk default-jre libncurses5-dev \
    libbz2-dev liblzma-dev

#Set wokingDir in /bin
WORKDIR /bin

#Download Cufflinks
RUN wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
#Unzip Cufflinks
RUN tar zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz
#Clean
RUN rm cufflinks-2.2.1.Linux_x86_64.tar.gz

#Download samtools from GitHub
RUN wget http://github.com/samtools/samtools/releases/download/1.5/samtools-1.5.tar.bz2
RUN tar --bzip2 -xf samtools-1.5.tar.bz2
WORKDIR /bin/samtools-1.5
RUN ./configure
RUN make
RUN rm /bin/samtools-1.5.tar.bz2

#Add Cufflinks and samtools to the path variable
ENV PATH $PATH:/bin/cufflinks-2.2.1.Linux_x86_64
ENV PATH $PATH:/bin/samtools-1.5

#Set the default Working Directory
WORKDIR /
