FROM ubuntu:14.04
MAINTAINER Peter Belmann

RUN apt-get update
RUN apt-get install -y wget git samtools g++ qt5-default libqt5xmlpatterns5-dev libqt5sql5-mysql git cmake 

#install sratoolkit
ENV SRA_TOOLKIT_DIR /sratoolkit.2.8.0-ubuntu64/bin
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.8.0/sratoolkit.2.8.0-ubuntu64.tar.gz
RUN tar xzvf sratoolkit.2.8.0-ubuntu64.tar.gz  --owner root --group root --no-same-owner
ENV PREFETCH ${SRA_TOOLKIT_DIR}/prefetch
ENV FASTQ_DUMP ${SRA_TOOLKIT_DIR}/fastq-dump

#install SeqPurge
RUN git clone --recursive https://github.com/imgag/ngs-bits.git
RUN make build_3rdparty -C /ngs-bits 
RUN make build_tools_release -C /ngs-bits 
ENV SEQPURGE /ngs-bits/bin/SeqPurge
