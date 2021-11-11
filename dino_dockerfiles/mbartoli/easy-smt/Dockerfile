# Version 0.0.1
FROM ubuntu:14.04

MAINTAINER Mike Bartoli "michael.bartoli@pomona.edu"

# base tools
RUN apt-get update
RUN apt-get install -y \
   unzip \
   build-essential \
   wget \
   g++ \
   git \
   subversion \
   automake \
   libtool \
   zlib1g-dev \
   libboost-all-dev \
   libbz2-dev \
   liblzma-dev \
   python-dev \
   libgoogle-perftools-dev 

RUN mkdir -p /home/moses
WORKDIR /home/moses
RUN mkdir moses-smt
RUN mkdir moses-models

RUN wget -O /home/moses/RELEASE-3.0.zip https://github.com/moses-smt/mosesdecoder/archive/RELEASE-3.0.zip
RUN unzip /home/moses/RELEASE-3.0.zip
RUN rm RELEASE-3.0.zip
RUN mv mosesdecoder-RELEASE-3.0 mosesdecoder

RUN wget -O giza-pp.zip "http://github.com/moses-smt/giza-pp/archive/master.zip" 
RUN unzip giza-pp.zip
RUN rm giza-pp.zip
RUN mv giza-pp-master giza-pp
WORKDIR /home/moses/giza-pp
RUN make

WORKDIR /home/moses

RUN mkdir external-bin-dir
RUN cp giza-pp/GIZA++-v2/GIZA++ external-bin-dir
RUN cp giza-pp/GIZA++-v2/snt2cooc.out external-bin-dir
RUN cp giza-pp/mkcls-v2/mkcls external-bin-dir

RUN wget -O cmph-2.0.tar.gz "http://downloads.sourceforge.net/project/cmph/cmph/cmph-2.0.tar.gz?r=&ts=1426574097&use_mirror=cznic"
RUN tar zxvf cmph-2.0.tar.gz

WORKDIR /home/moses/cmph-2.0
RUN ./configure
RUN make
RUN make install
WORKDIR /home/moses

RUN wget -O irstlm-5.80.08.tgz "http://downloads.sourceforge.net/project/irstlm/irstlm/irstlm-5.80/irstlm-5.80.08.tgz?r=&ts=1342430877&use_mirror=kent"
RUN tar zxvf irstlm-5.80.08.tgz
WORKDIR /home/moses/irstlm-5.80.08/trunk
RUN /bin/bash -c "source regenerate-makefiles.sh"
RUN ./configure -prefix=/home/moses/irstlm
RUN make
RUN make install

WORKDIR /home/moses

ENV IRSTLM /home/moses/irstlm
WORKDIR /home/moses/mosesdecoder

#RUN ./bjam -a --with-irstlm=/home/moses/irstlm --serial --with-xmlrpc-c=/usr/ --with-cmph=/home/moses/cmph-2.0

#RUN ./bjam -j8

WORKDIR /home/moses/moses-smt
