FROM ubuntu

MAINTAINER Tao Zhang "forrestzhang1982@gmail.com"

RUN apt-get update && apt-get install -y  build-essential \
                                                                  zlib1g-dev \
                                                                  zlibc \
                                                                  openjdk-7-jre \
                                                                  git \
                                                                  libboost-dev \
                                                                  autoconf \
                                                                  libncursesw5-dev \
                                                                  libncurses5 \
                                                                  ncurses-dev \
                                                                  libboost-thread-dev \
                                                                  python3-pip \
								                                                  unzip

RUN apt-get update && \
         apt-get install -y  software-properties-common  && \
        add-apt-repository ppa:j-4/vienna-rna && \
	      apt-get -qq update && \
	      apt-get install -y vienna-rna bowtie wget libpdf-api2-perl

RUN mkdir /opt/software
WORKDIR /opt/software
ADD https://www.mdc-berlin.de/43969303/en/research/research_teams/systems_biology_of_gene_regulatory_elements/projects/miRDeep/mirdeep2_0_0_7.zip /opt/software/
RUN wget ftp://selab.janelia.org/pub/software/squid/squid-1.9g.tar.gz
ADD http://bioinformatics.psb.ugent.be/supplementary_data/erbon/nov2003/downloads/randfold-2.0.tar.gz /opt/software/


#WORKDIR /opt/software
RUN tar zxvf squid-1.9g.tar.gz
WORKDIR /opt/software/squid-1.9g
RUN ./configure && make && make install
WORKDIR /opt/software
RUN tar zxvf randfold-2.0.tar.gz
WORKDIR /opt/software/randfold-2.0
RUN make
WORKDIR /opt/software
RUN unzip mirdeep2_0_0_7.zip && mv mirdeep2_0_0_7 mirdeep2
ENV PATH /opt/software/randfold-2.0:/opt/software/mirdeep2:$PATH

RUN mkdir /rnadata
WORKDIR /rnadata
