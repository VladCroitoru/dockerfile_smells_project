FROM ubuntu:17.10

MAINTAINER Fabrizio Torelli (hellgate75@gmail.com)

ARG DEBIAN_FRONTEND=noninteractive
ARG RUNLEVEL=1

ENV JAVA_VERSION=8u131 \
    JAVA_RELEASE=b11 \
    JAVA_HOME=/usr/java/default \
    PATH=$PATH:/usr/java/default/bin \
    BASH_ENV=/etc/profile




USER root

#RUN dpkg --force-help && exit 1

RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/no-cache && \
  echo "deb http://mirror.math.princeton.edu/pub/ubuntu trusty main universe" >> /etc/apt/sources.list && \
  apt-get update -q -y && \
  apt-get dist-upgrade -y && \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && apt-get -q -y install apt-utils && apt-get -q -y -o Dpkg::Options::="--force-confold,overwrite,confdef" \
  install --no-install-recommends wget curl tar sudo openssh-client rsync build-essential

RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
  ssh-keygen -q -N "" -t rsa -f /root/.ssh/id_rsa && cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys

RUN apt-get -q -y -o Dpkg::Options::="--force-confold,overwrite,confdef" install --no-install-recommends openssh-server ca-certificates openssl rpm \
    python-pip python-sklearn python-pandas python-numpy python-matplotlib software-properties-common python-software-properties ssh pdsh net-tools tmux
    # this latest package makes available add-apt-repository commnd

RUN add-apt-repository -y ppa:webupd8team/java && \
    apt-get update -q && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
    DEBIAN_FRONTEND=noninteractive  apt-get install -y oracle-java8-installer && \
    mkdir -p /usr/java && \
    ln -s /usr/lib/jvm/java-8-oracle /usr/java/default && \
    echo "===> clean up..."  && \
    rm -rf /var/cache/apt/archives/*.deb  && \
    apt-get -y autoremove  && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /
