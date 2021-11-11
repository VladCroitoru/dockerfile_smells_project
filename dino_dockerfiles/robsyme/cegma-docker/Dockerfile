FROM ubuntu:14.04
MAINTAINER Robert Syme <robsyme@gmail.com>

RUN sed 's/main$/main universe/' -i /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get upgrade -y


# Install the basics
RUN apt-get install -y wget unzip build-essential


# Install Genewise
RUN apt-get install -y wise && \
    mkdir -p /opt/genewise && \
    cd /opt/genewise && \
    wget http://korflab.ucdavis.edu/datasets/cegma/wise2.2.3-rc7.tar.gz && \
    tar xfz wise*.tar.gz && \
    rm wise*.tar.gz && \
    ln -s wise2.2.3-rc7 current


# Install HMMER
RUN apt-get install -y hmmer


# Install geneid
RUN mkdir -p /opt/geneid && \
    cd /opt/geneid && \
    wget ftp://genome.crg.es/pub/software/geneid/geneid_v1.4.4.Jan_13_2011.tar.gz && \
    tar xfz geneid*.tar.gz && \
    rm geneid*.tar.gz && \
    mv geneid current && \
    cd current && \
    make

# Install ncbi-blast+
RUN apt-get install -y ncbi-blast+


# Install CEGMA
ADD http://github.com/KorfLab/CEGMA_v2/archive/v2.5.tar.gz /opt/
RUN cd /opt/ && \
    tar -xzvf v2.5.tar.gz && \
    mv CEGMA_v2-2.5 cegma && \
    cd cegma && \
    make

ENV WISECONFIGDIR /opt/genewise/current/wisecfg/
ENV CEGMA /opt/cegma
ENV PERL5LIB $CEGMA/lib
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$CEGMA/bin:/opt/geneid/current/bin/
