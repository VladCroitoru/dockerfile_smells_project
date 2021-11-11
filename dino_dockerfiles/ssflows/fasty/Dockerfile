FROM ubuntu:16.04

ENV TIMESTAMP 10-01-2017

RUN apt-get update -qq && apt-get install -y lsb-release
RUN echo "debconf debconf/frontend select Teletype" | debconf-set-selections
RUN echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main restricted universe" > /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-updates main restricted universe" >> /etc/apt/sources.list
RUN echo "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)-security main restricted universe" >> /etc/apt/sources.list
RUN apt-get update -qq && apt-get upgrade -y && apt-get install -y curl wget build-essential git libssl-dev libreadline-dev zlib1g-dev software-properties-common dh-autoreconf

RUN mkdir /jemalloc && cd /jemalloc &&\
    wget https://github.com/jemalloc/jemalloc/releases/download/3.6.0/jemalloc-3.6.0.tar.bz2 &&\
    tar -xjf jemalloc-3.6.0.tar.bz2 && cd jemalloc-3.6.0 && ./configure --prefix=/usr && make && make install &&\
    cd / && rm -rf /jemalloc

RUN echo 'gem: --no-document' >> /usr/local/etc/gemrc &&\
    mkdir /src && cd /src && git clone https://github.com/sstephenson/ruby-build.git &&\
    cd /src/ruby-build && ./install.sh &&\
    cd / && rm -rf /src/ruby-build && ruby-build 2.3.3 /usr/local

RUN gem install bundler &&\
    rm -rf /usr/local/share/ri/2.3.0/system

RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list &&\
    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 &&\
    gpg -a --export E084DAB9 | apt-key add - &&\
    apt-get update -qq &&\
    apt-get install -y --no-install-recommends r-base bioperl apt-utils bioperl-run libexpat-dev gengetopt

#####################
#   Bioconductor    #
#####################

RUN R -e "source('https://bioconductor.org/biocLite.R');biocLite('qvalue')"

#####################
#       PAML        #
#####################

RUN mkdir -p /usr/src/paml \
  && curl -SL "http://abacus.gene.ucl.ac.uk/software/paml4.9c.tgz" \
  | tar zxC /usr/src/paml \
  && cd /usr/src/paml/paml4.9c/src \
  && make -j"$(nproc)" \
  && mv codeml /usr/bin/ \
  && mv baseml /usr/bin/ \
  && mv basemlg /usr/bin/ \
  && mv chi2 /usr/bin/ \
  && mv evolver /usr/bin/ \
  && mv infinitesites /usr/bin/ \
  && mv mcmctree /usr/bin/ \
  && mv pamp /usr/bin/ \
  && mv yn00 /usr/bin/ \
  && rm -rf /usr/src/paml

#####################
#      Guidance     #
#####################
RUN mkdir -p /usr/src/guidance \
  && cd /usr/src/guidance \
  && wget "https://github.com/anzaika/guidance/archive/v2.01.tar.gz" \
  && tar xvf v2.01.tar.gz \
  && cd /usr/src/guidance/guidance-2.01 \
  && sed -i 's/time\ -p//g' /usr/src/guidance/guidance-2.01/www/Guidance/exec/HoT_COS_GUIDANCE2.pl \
  && sed -i 's/time\ -p//g' /usr/src/guidance/guidance-2.01/www/Guidance/exec/HoT/COS.pl \
  && make -j"$(nproc)"

##########################
#       DNDSTolls        #
##########################
RUN mkdir -p /usr/src/dndstools \
  && git clone https://anzaika@bitbucket.org/Davydov/dndstools.git /usr/src/dndstools/ \
  && cd /usr/src/dndstools \
  && chmod +x cdmw.py \
  && mv cdmw.py /usr/local/bin/ \
  && chmod +x mlc2csv.py \
  && mv mlc2csv.py /usr/local/bin/ \
  && rm -rf /usr/src/dndstools

#####################
#      PhyML        #
#####################

RUN mkdir -p /usr/src/beagle &&\
    cd /usr/src &&\
    git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git beagle &&\
    cd /usr/src/beagle &&\
    apt-get -y install openjdk-8-jdk checkinstall &&\
    ./autogen.sh &&\
    ./configure &&\
    make &&\
    make install &&\
    rm -rf /usr/src/beagle

RUN mkdir -p /usr/src/phyml &&\
  cd /usr/src &&\
  git clone https://github.com/anzaika/phyml.git &&\
  cd /usr/src/phyml &&\
  sh ./autogen.sh &&\
  sh ./configure &&\
  make -j"$(nproc)" &&\
  mv src/phyml /usr/local/bin &&\
  rm -rf /usr/src/phyml

#####################
#       mafft       #
#####################

ENV MAFFT_VERSION 7.273

RUN mkdir -p /usr/src/mafft \
  && curl -SL "http://mafft.cbrc.jp/alignment/software/mafft-$MAFFT_VERSION-with-extensions-src.tgz" \
  | tar xvzC /usr/src/mafft \
  && cd /usr/src/mafft/mafft-$MAFFT_VERSION-with-extensions/core \
  && make -j"$(nproc)" \
  && make install \
  && rm -rf /usr/src/mafft

#####################
# fastcodeml-source #
#####################

RUN apt-get install -y --no-install-recommends \
    gfortran cmake-curses-gui \
    libopenblas-dev liblapack-dev libnlopt-dev libboost-all-dev

ENV OPENBLAS_NUM_THREADS 1
# RUN mkdir -p /usr/src/openblas \
#   && curl -SL "https://github.com/xianyi/OpenBLAS/archive/v0.2.19.tar.gz" \
#   | tar xvzC /usr/src/openblas \
#   && cd /usr/src/openblas/OpenBLAS-0.2.19 \
#   && make -j"$(nproc)" \
#   && make install

# ENV BLAS_LIB_DIR "/opt/OpenBLAS/lib"
# ENV LAPACK_LIB_DIR "/opt/OpenBLAS/include"

ENV MATH_LIB_NAMES openblas;lapack
COPY fast_build_config.txt /usr/src/CMakeLists.txt
RUN cd /usr/src \
    && git clone https://gitlab.isb-sib.ch/phylo/fastcodeml.git \
    && cd fastcodeml \
    && cp ../CMakeLists.txt . \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j"$(nproc)" \
    && mv fast /usr/bin/ \
    && rm -rf /usr/src/fastcodeml

#####################

ADD . /installdir
WORKDIR /installdir
RUN bundle install -j6

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENTRYPOINT ["bundle", "exec", "./bin/fasty"]
# ENTRYPOINT ["bundle", "exec", "rspec"]
