# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM ubuntu:14.04

RUN \
  sed -Ei 's/^# (deb.*xenial-backports.*)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y autoconf automake byobu bzip2 curl gfortran git htop lzma man sudo unzip vim wget && \
  apt-get install -y libbz2-dev libcurl4-openssl-dev libgsl0-dev liblzma-dev libncurses5-dev libpcre3-dev \
    libreadline6-dev libssl-dev python-dev python-pip zlib1g-dev && \
  rm -rf /var/lib/apt/lists/*

# get NBCI Toolkit
WORKDIR /tmp
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/ngs/1.3.0/ngs-sdk.1.3.0-linux.tar.gz && \
    tar xzvf ngs-sdk.1.3.0-linux.tar.gz

# Install  StarAligner
WORKDIR /star_install
RUN wget https://github.com/alexdobin/STAR/archive/2.5.3a.tar.gz && \
    tar -xzf 2.5.3a.tar.gz && \
    cd STAR-2.5.3a 
    
ENV PATH="/star_install/STAR-2.5.3a/bin/Linux_x86_64:${PATH}"

RUN    pip install awscli 

COPY common/container_scripts/runS3OnBatch.sh /usr/local/bin/runS3OnBatch.sh
COPY common/container_scripts/runLocal.sh /usr/local/bin/runLocal.sh

RUN chmod ugo+x /usr/local/bin/runS3OnBatch.sh /usr/local/bin/runLocal.sh 

RUN apt-get update && \
   apt-get install zip --yes
RUN cpan -f Archive::Zip

CMD ["/usr/local/bin/runS3OnBatch.sh" ]

