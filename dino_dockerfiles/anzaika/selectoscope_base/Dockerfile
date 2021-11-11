FROM anzaika/ruby

ENV TIMESTAMP 10-01-2017

# Additional packages
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" >> /etc/apt/sources.list &&\
    gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 &&\
    gpg -a --export E084DAB9 | apt-key add - &&\
    apt-get update -qq &&\
    apt-get install -y --no-install-recommends r-base bioperl apt-utils bioperl-run libexpat-dev gengetopt

RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash - &&\
    apt-get install -y nodejs &&\
    npm install webpack webpack-dev-server -g

# Installing BioPerl this way is very slow and I even don't know if it's the right way
# #####################
# #      BioPerl      #
# #####################
#
# RUN apt-get install -y --no-install-recommends libexpat-dev libcgi-session-perl libclass-base-perl libgd-gd2-perl \
#   && PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Bundle::CPAN;quit' \
#   && PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Text::Shellwords' \
#   && PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Bundle::LWP' \
#   && PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Bio::SeqIO'

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

# ####################
# #    Muscle        #
# ####################
# RUN mkdir -p /usr/src/muscle \
#   && curl -SL "http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz" \
#   | tar xvzC /usr/src/muscle \
#   && cd /usr/src/muscle \
#   && mv muscle3.8.31_i86linux64 /usr/local/bin/muscle \
#   && rm -rf /usr/src/muscle

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
#      Gblocks      #
#####################

RUN mkdir -p /usr/src/gblocks \
  && curl -SL "http://molevol.cmima.csic.es/castresana/Gblocks/Gblocks_Linux64_0.91b.tar.Z" \
  | tar xvzC /usr/src/gblocks \
  && cd /usr/src/gblocks/Gblocks_0.91b \
  && cp Gblocks /usr/local/bin \
  && rm -rf /usr/src/gblocks

#####################
# fastcodeml-source #
#####################

ENV MATH_LIB_NAMES openblas;lapack
COPY fast_build_config.txt /usr/src/CMakeLists.txt
RUN apt-get install -y --no-install-recommends \
    gfortran cmake-curses-gui libopenblas-dev \
    libopenblas-base liblapack-dev libnlopt-dev libboost-all-dev \
    && cd /usr/src \
    && git clone https://gitlab.isb-sib.ch/phylo/fastcodeml.git \
    && cd fastcodeml \
    && cp ../CMakeLists.txt . \
    && cmake . \
    && make -j"$(nproc)" \
    && mv fast /usr/bin/ \
    && rm -rf /usr/src/fastcodeml
#####################

#####################
# TCoffee
#####################
ENV USER_BIN /usr/bin
RUN git clone https://github.com/cbcrg/tcoffee.git /usr/src/tcoffee &&\
    cd /usr/src/tcoffee/compile &&\
    make -j"$(nproc)" t_coffee &&\
    rm -rf /usr/src/tcoffee
#####################


RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
