# Dockerfile
#
# Requires
#   execute-only: bash
#
FROM ubuntu:latest
LABEL description="SystemC-Complete - Tools to compile SystemC with GCC & Clang under Ubuntu" \
      maintainer="David Black <david.black@doulos.com>" alternate="dcblack@mac.com"

# Eliminate interactive queries during build
ENV DEBIAN_FRONTEND=noninteractive\
    TZ=US/Central

RUN perl -pi -e 's{^# +(deb http://archive.canonical.com/ubuntu bionic partner)}{$1}' /etc/apt/sources.list \
 && echo "$TZ" >/etc/timezone

RUN apt-get -y update && apt-get -y install \
    apt apt-utils

# Compiler tools
RUN apt-get -y update && apt-get -y install \
    astyle \
    autoconf \
    automake \
    bison \
    cgdb \
    clang \
    clang-tidy \
    clang-tools \
    cppcheck \
    doxygen \
    flex \
    g++ \
    gdb

# Libraries and automation
RUN apt-get -y update && apt-get -y install \
    git \
    libsecret-1-dev \
    libsecret-1-0 \
    graphviz \
    libboost-all-dev \
    libyaml-cpp-dev \
    rapidjson-dev \
    locales \
    make \
    ninja-build \
    cmake \
    graphviz \
    doxygen \
    perl-doc \
    python3-pip

# Useful in an interactive context
RUN apt-get -y update && apt-get -y install \
    rsync \
    silversearcher-ag \
    sudo \
    time \
    tree \
    vim \
    wget \
    yamllint \
    && perl -pi -e 'if( m/^root/ ) { print; s/root/sc_user/; }' /etc/sudoers


ENV APPS=/apps \
    CMAKE_VERSION=3.14 CMAKE_BUILD=4\
    CC=gcc CXX=g++ \
    BOLD="[01m" \
    CBLK="[30m" CRED="[31m" CGRN="[32m" CYLW="[33m" \
    CBLU="[34m" CMAG="[35m" CCYN="[36m" CWHT="[37m" \
    NONE="[00m"
# RED,GRN,YLW,BLU,MAG,CYN,WHT,BLK

COPY apps/setup.profile $APPS/
COPY apps/src $APPS/src/
COPY apps/systemc $APPS/systemc/

# Install cmake if not available from repo
# WORKDIR $APPS/src
# RUN pip3 install -U sphinx && $APPS/bin/install-cmake

# Install SystemC, CCI and other components
#COPY apps/src/systemc  $APPS/src/systemc
WORKDIR $APPS/src
COPY apps/bin/install-systemc $APPS/bin/install-systemc
ENV SYSTEMC_HOME=/apps/systemc
RUN $APPS/bin/install-systemc

# Setup CCI
ENV CCI_HOME=/apps/cci
WORKDIR $APPS
COPY apps/bin/install-cci $APPS/bin/install-cci
COPY apps/cci $APPS/cci/
RUN ln -s $APPS/src/systemc/src $SYSTEMC_HOME/src \
    && $APPS/bin/install-cci

RUN pip3 install conan
# RUN apt-get -y update && apt-get -y install \
#     libc++

# Stuff that changes more frequently
COPY apps/bin $APPS/bin/
COPY apps/.vim    $APPS/.vim/
COPY apps/include $APPS/include/
COPY apps/cmake   $APPS/cmake/
COPY apps/make    $APPS/make/
COPY apps/sc-templates $APPS/sc-templates/
COPY apps/scc     $APPS/scc/
# WORKDIR $APPS
# RUN git clone git@github.com:dcblack/sc-templates.git

# Minor patches to aid some setup assumptions
RUN echo "Set disable_coredump false" >> /etc/sudo.conf \
 && ln -s $SYSTEMC_HOME/lib $SYSTEMC_HOME/lib-linux64 \
 && ln -s $CCI_HOME/src     $CCI_HOME/include

ENV USER=sc_user \
    HOME=/home/sc_user \
    EMAIL=sc_user@doulos.com

RUN adduser --home $HOME --shell /bin/bash --ingroup users --disabled-password \
      --gecos "SystemC developer" $USER \
 && printf "%s\n%s\n" $EMAIL $EMAIL | passwd $USER
COPY home $HOME/
RUN chown -R $USER $APPS $HOME \
 && chgrp -R users $APPS $HOME \
 && chmod u=rwx,g+sx $APPS $HOME/bin\
 && find $APPS -type f -name '[^.]*' ! -path '*/[.]*' -exec chmod a-w {} \; \
 && chmod g+s $HOME $HOME/bin \
 && mkdir -p $HOME/work

RUN locale-gen en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8' \
    TZ=US/Central \
    TERM=xterm-color
WORKDIR $HOME/work
USER $USER:users
