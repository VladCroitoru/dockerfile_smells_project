FROM ubuntu:16.04

RUN \
  sed -Ei 's/^# (deb.*xenial-backports.*)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y autoconf automake byobu bzip2 curl gfortran git htop lzma man sudo unzip vim wget && \
  apt-get install -y libbz2-dev libcurl4-openssl-dev libgsl0-dev liblzma-dev libncurses5-dev libpcre3-dev \
    libreadline6-dev libssl-dev python-dev python-pip zlib1g-dev && \
  add-apt-repository ppa:webupd8team/java -y && \
  apt-get update && \
  echo oracle-java9-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
  apt-get install -y oracle-java9-installer && \
  apt-get install -y oracle-java9-set-default && \
  rm -rf /var/lib/apt/lists/*
