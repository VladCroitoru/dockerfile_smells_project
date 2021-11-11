FROM ubuntu:bionic
MAINTAINER Julio Delgado <julio.delgadomangas@gmail.com>
ENV USER root
ENV HOME /root

RUN apt-get update && apt-get install software-properties-common wget -y
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - && \
        apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-6.0 main" && \
        apt-get update && \
        apt-get install -y clang-6.0

RUN add-apt-repository ppa:kelleyk/emacs && apt-get update \
    && apt-get install -y curl \
                       file \
                       git \
                       emacs26 \
                       gcc \
                       g++ \
                       libclang-6.0-dev \
                       cmake \
                       python3-pip \
                       libboost-all-dev \
                       zlib1g-dev


# RTAGS
RUN mkdir -p /opt/src && cd /opt/src/ && git clone --recursive https://github.com/Andersbakken/rtags.git && \
    cd rtags && cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1 . && make install -j2 && cd .. && rm -rf rtags
#ENV PATH "${PATH}:/opt/src/rtags/bin/"

# the DOOM emacs depends the latest git.
RUN add-apt-repository ppa:git-core/ppa && apt install -y git
# use a specific commit to avoid doom-emacs broken update
RUN git clone https://github.com/hlissner/doom-emacs ~/.emacs.d && cd ~/.emacs.d && git checkout 2731685
RUN printf 'y\ny' | ~/.emacs.d/bin/doom -y install

# update doom config
RUN git clone https://github.com/Superjomn/emacs-dev.git && echo 0 && cp emacs-dev/.doom.d/* ~/.doom.d/ && ~/.emacs.d/bin/doom sync
# fix irony missing file error
RUN mkdir -p /root/.emacs.d/.local/etc/irony
RUN touch /root/.emacs.d/.local/etc/irony/cdb-json-projects

# build emacs by source to avoid X system segment fault
RUN apt-get install -y libxaw7-dev build-essential texinfo libx11-dev libjpeg-dev libpng-dev libgif-dev libtiff-dev libncurses-dev gnutls-dev
RUN wget https://ftpmirror.gnu.org/emacs/emacs-27.1.tar.gz && \
	tar xvf emacs-27.1.tar.gz && \
	cd emacs-27.1 &&\
	./configure --with-x-toolkit=lucid &&\
	make -j2 &&\
	make install

# enable vterm
RUN apt install libtool-bin

# clean
RUN apt autoremove

RUN git config --global credential.helper store
