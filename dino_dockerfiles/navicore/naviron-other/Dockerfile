FROM centos:7

MAINTAINER Ed Sweeney <ed@onextent.com>

WORKDIR /root

RUN yum update -y && yum install -y epel-release && yum clean all

RUN yum install -y \
  ncurses-devel \
  python \
  python-devel \
  python-pip \
  zsh \
  readline-devel \
  p7zip \
  p7zip-plugins \
  bison \
  bzip2 \
  bzip2-devel \
  cmake \
  curl-devel \
  cronie \
  czmq \
  expat-devel \
  flex \
  gcc \
  gcc-c++ \
  gcc-gfortran \
  gdb \
  gettext-devel \
  glibc-devel \
  libattr-devel \
  libcurl \
  libcurl-devel \
  libedit-devel libffi-devel \
  libgcc \
  libstdc++-static \
  libtool \
  m4 \
  make \
  nload \
  htop \
  openssl \
  openssl098e \
  openssl-devel \
  patch \
  unzip \
  sqlite \
  sqlite-devel \
  telnet \
  git \
  wget \
  zlib \
  zlib-devel \
  zip \
  java-1.8.0 \
  && yum clean all

ENV PATH /usr/local/sbin:/usr/local/bin:$PATH

ENV CPATH /usr/include/glpk

ENV LD_LIBRARY_PATH /usr/local/lib:/usr/local/lib64

# Makes git use https by default
RUN git config --global url."https://".insteadOf git://

# llvm needs CMake 2.8.12.2 or higher
# https://cmake.org/download/
ENV CMAKE_VER_MAJ 3.10
ENV CMAKE_VER_MIN .1
ENV CMAKE_VER $CMAKE_VER_MAJ$CMAKE_VER_MIN

RUN wget https://cmake.org/files/v$CMAKE_VER_MAJ/cmake-$CMAKE_VER.tar.gz \
  && tar xf cmake-$CMAKE_VER.tar.gz && cd cmake-$CMAKE_VER \
  && ./bootstrap && make -j"$(nproc --all)" && make -j"$(nproc --all)" install \
  && cd .. && rm -rf cmake-$CMAKE_VER && rm -f cmake-$CMAKE_VER.tar.gz

ENV CMAKE_ROOT /usr/local/share/cmake-$CMAKE_VER_MAJ

# Improve link to shared libraries
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib64/R/lib:/usr/local/lib:/lib:/usr/lib/jvm/jre/lib/amd64/server:/usr/lib/jvm/jre/lib/amd64:/usr/lib/jvm/java/lib/amd64:/usr/java/packages/lib/amd64:/lib:/usr/lib:/usr/local/lib

# node and lua
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && yum install -y nodejs \
  && curl -R -O http://www.lua.org/ftp/lua-5.3.4.tar.gz && tar zxf lua-5.3.4.tar.gz && cd lua-5.3.4 && make linux install && cd .. && rm -rf lua* \
  && curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-rpm.repo && yum install -y sbt

