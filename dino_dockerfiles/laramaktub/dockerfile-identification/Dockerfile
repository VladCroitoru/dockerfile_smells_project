FROM ubuntu:xenial

RUN  apt-get -y update \
      && apt-get -y upgrade 

##### Install the basics
RUN apt-get install -y  git-all wget unzip bzip2 build-essential gcc-multilib apt-utils zlib1g-dev software-properties-common python-setuptools python-dev python-numpy

RUN apt-get install -y zlib1g-dev libncurses5-dev

RUN  apt-get install --yes ncbi-blast+

#install Blat
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat -P /usr/local/bin
RUN chmod a+x /usr/local/bin/blat

RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz \
    && tar xf hmmer-3.1b2.tar.gz  \
    && cd hmmer-3.1b2  \
    && ./configure  \
    && make  \
    && make install 


# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer


RUN cd /opt/ \
    && mkdir my_interproscan \
    && cd my_interproscan
RUN wget ftp://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/5RC1/interproscan-5-64-bit-RC1.tar.gz
RUN tar -pxvzf interproscan-5-*-bit-RC1.tar.gz
ENV PATH=/opt/interproscan-5-RC1/:$PATH

## Including OneData client



CMD /bin/bash -l

