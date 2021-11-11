FROM  cfljam/pyrat_genetics

MAINTAINER John McCallum john.mccallum@plantandfood.co.nz

# Set noninterative mode
ENV DEBIAN_FRONTEND noninteractive

################## BEGIN INSTALLATION ######################

## ipython/ipython is 14.04 (trusty) and ncurses is for samtools and precise dependencies are unresolved
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list


##Install Prerequisites and BioPython
RUN set -xe ;\
  apt-get update;\
  apt-get -y upgrade;\
  apt-get -y dist-upgrade ;\
  apt-get autoremove;\
  apt-get autoclean;\
  apt-get install -y \
  build-essential \
  python-setuptools \
  python-biopython

### Install python packages
### Note explicit use of Py version to avoid pip version issues
ADD requirements.txt /tmp/
RUN set -xe ;\
python2 /usr/local/bin/pip   --default-timeout=100 install -r /tmp/requirements.txt


ENV PERL5LIB /usr/local/lib/perl5

## Install VCF lib
RUN set -xe ;\
  git clone --recursive https://github.com/ekg/vcflib.git ;\
  cd vcflib ;\
  make ;\
  cp ./bin/* /usr/local/bin/

## Install HTS lib
RUN set -xe ;\
  git clone --branch=develop https://github.com/samtools/htslib.git ;\
  cd htslib ;\
  make ;\
  make test ;\
  make install

## Install samtools
RUN set -xe ;\
  git clone --branch=develop https://github.com/samtools/samtools.git ;\
  cd samtools ;\
  make HTSDIR=/tmp/htslib;\
  make test ;\
  make install

## Install bedtools plus Python interface
RUN set -xe ;\
   apt-get  install -y  bedtools

### Install Exonerate
RUN set -xe ;\
  git clone https://github.com/nathanweeks/exonerate.git ;\
  cd exonerate ;\
  git checkout v2.4.0;\
  autoreconf -f -i ;\
  ./configure ;\
  make ;\
  make check ;\
  make install

## Install BCF tools
RUN set -xe ;\
  git clone --branch=develop https://github.com/samtools/bcftools.git ;\
  cd bcftools ;\
  make HTSDIR=/tmp/htslib;\
  make test ;\
  make install


## Install VCF tools
RUN set -xe ;\
 git clone https://github.com/vcftools/vcftools;\
cd vcftools; \
 ./autogen.sh;\
 ./configure;\
 make;\
make install

##########################################

### Launch ipynb as default

CMD ipython notebook --ip=0.0.0.0 --port=8888 --no-browser

##################### INSTALLATION END #####################

## TEST
ADD test-suite.sh /tmp/test-suite.sh
RUN ./test-suite.sh

## Clean up
RUN rm -rf /tmp/*
