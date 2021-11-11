FROM ubuntu:16.04
LABEL maintainer="Hoang Tung Dinh"

ENV DEBIAN_FRONTEND noninteractive

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV LD_LIBRARY_PATH /ThirdParties/JSCIPOpt/build

RUN apt-get update && \
  apt-get dist-upgrade -y

# Remove any existing JDKs
RUN apt-get --purge remove openjdk*

# Install Oracle's JDK
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" > /etc/apt/sources.list.d/webupd8team-java-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
RUN apt-get update \
  && apt-get install -y --no-install-recommends oracle-java8-installer \
  && apt-get clean all 

# Install some necessary packages
RUN apt-get install -y wget git zsh vim g++ make cmake expect \
  && git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
  && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
  && chsh -s /bin/zsh

# Directory for all third party dependencies
RUN mkdir /ThirdParties

# Install IPOPT
ADD Ipopt-3.12.7.tgz /ThirdParties/
RUN apt-get install -y libopenblas-dev \
  && cd /ThirdParties/Ipopt-3.12.7/ThirdParty/Mumps \
  && ./get.Mumps \
  && cd /ThirdParties/Ipopt-3.12.7/ThirdParty/Metis \
  && ./get.Metis \
  && cd /ThirdParties/Ipopt-3.12.7 \
  && mkdir build \
  && cd build \
  && ../configure \
  && make \
  && make install

# Install SCIP
ADD scipoptsuite-4.0.0.tgz /ThirdParties/
ADD install_scip /ThirdParties/
RUN chmod +x /ThirdParties/install_scip \
  && sync \
  && mv /ThirdParties/install_scip /ThirdParties/scipoptsuite-4.0.0 \
  && cd /ThirdParties/scipoptsuite-4.0.0 \
  && ./install_scip

# Install JSCIPOPT
RUN cd /ThirdParties \
  && git clone https://github.com/hoangtungdinh/JSCIPOpt.git \
  && cd /ThirdParties/JSCIPOpt \
  && mkdir lib \
  && cd lib \
  && ln -s /ThirdParties/scipoptsuite-4.0.0/lib/libscipopt.so libscipopt.so \
  && ln -s /ThirdParties/scipoptsuite-4.0.0/scip-4.0.0/src scipinc \
  && cd .. \
  && mkdir build \
  && cd build \
  && cmake .. \
  && make


VOLUME /app
WORKDIR /app

# To test your application, mount it to /app
