FROM centos:7
MAINTAINER Marcus R. Breese <marcus.breese@ucsf.edu>

COPY src/STAR_2.4.2a.tar.gz /tmp
COPY src/bcftools-1.3.tar.bz2 /tmp
COPY src/bwa-0.7.12.tar.bz2 /tmp
COPY src/samtools-1.2.tar.bz2 /tmp
COPY src/cgpipe /usr/local/bin
COPY src/cgseq /usr/local/bin
COPY src/ngsutilsj /usr/local/bin

RUN yum update -y && \
    yum install -y vim-common gcc-c++ gcc make ncurses-devel zlib-devel tar bzip2 java-1.8.0-openjdk-headless ant tar which && \
    yum clean all && \
    cd /tmp && \
    tar -xf samtools-1.2.tar.bz2 && cd samtools-1.2 && make install && \
    cd htslib-1.2.1 && make install && cd ../.. && \
    tar -xf bwa-0.7.12.tar.bz2 && cd bwa-0.7.12 && make && cp bwa /usr/local/bin  && cd .. && \
    tar -xf bcftools-1.3.tar.bz2 && cd bcftools-1.3 && make && cp bcftools vcfutils.pl /usr/local/bin && cd .. && \
    tar -xf STAR_2.4.2a.tar.gz && cp STAR-STAR_2.4.2a/bin/Linux_x86_64/* /usr/local/bin && \
    cd / && rm -rf /tmp/* && mkdir /scratch && mkdir /data && chmod +x /usr/local/bin/* && yum clean all

VOLUME /scratch
VOLUME /data

WORKDIR /data
