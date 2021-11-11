#################################################################
# Dockerfile
#
# Version:          0.0.1
# Software:         pAss
# Software Version: 0.0.2
# Description:      A gene centric metagenomics assembly and annotation pipeline
# Website:          https://github.com/etheleon/pAss
# Tags:             Genomics Metagenomics
# Provides:         MEGAN, MUSCLE, R, XVFB, PERL, BLAST
# Base Image:       ubuntu
#################################################################

FROM ubuntu:16.04

#Java###############################
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean

#NCBI BLAST##############################
RUN apt-get install -y ncbi-blast+

WORKDIR /tmp

#MEGAN#############################
RUN apt-get update && apt-get install -y xvfb
RUN wget -nv http://ab.inf.uni-tuebingen.de/data/software/megan5/download/MEGAN_unix_5_11_3.sh
RUN perl -E 'say join "\n", "", 1, "", 1, "", "", "", 38000, n, ""' > /tmp/megan_install_v5
#COPY megan_install_v5 /tmp
RUN bash MEGAN_unix_5_11_3.sh < /tmp/megan_install_v5

#Dependencies############################

RUN apt-get update && \
    apt-get install -y r-base && \
    apt-get install -y curl && \
    apt-get install -y make && \
    apt-get install -y git

RUN wget http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz && \
    tar zvxf muscle3.8.31_i86linux64.tar.gz
RUN cp /tmp/muscle3.8.31_i86linux64 /usr/bin/muscle

RUN R --slave -e 'install.packages("tidyverse", repos="http://cran.bic.nus.edu.sg/")'
RUN R --slave -e 'source("http://bioconductor.org/biocLite.R"); biocLite("Biostrings")'

#Perl Stuff
RUN apt-get install perl-doc
RUN curl -L https://cpanmin.us | perl - App::cpanminus && \
    cpanm local::lib Carton Module::Install Minilla Devel::CheckBin Module::Install Modern::Perl Moo Bio::SeqIO Statistics::Basic Statistics::R namespace::clean Set::IntervalTree Getopt::Lucid Parallel::ForkManager Array::Utils List::MoreUtils Test::More

#################### INSTALLATION ENDS ##############################
MAINTAINER Wesley GOI <wesley@bic.nus.edu.sg>
