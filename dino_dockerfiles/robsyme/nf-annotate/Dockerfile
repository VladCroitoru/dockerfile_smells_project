FROM ubuntu:17.10

MAINTAINER Rob Syme <rob.syme@gmail.com>

RUN apt-get update \
&& apt-get install -qqy \
aragorn \
bowtie2 \
build-essential \
cufflinks \
default-jre \
exonerate \
genometools \
git \
iputils-ping \
libbamtools-dev \
libbio-perl-perl \
libboost-graph-dev \
libboost-iostreams-dev \
libdbi-perl \
libgsl-dev \ 
libio-string-perl \
liblpsolve55-dev \
libmysqlclient-dev \
libparallel-forkmanager-perl \
libpng-dev \
libsqlite3-dev \
libssl-dev \
libsuitesparse-dev \
lua5.1 \
openssl \
python \
python-dev \
python-numpy \
r-base \
r-cran-dplyr \
r-cran-magrittr \
r-cran-phangorn \
r-cran-reshape2 \
rsync \
tabix \
time \
unzip \
wget \
zlib1g-dev

WORKDIR /usr/local

# Install Augustus
RUN wget http://bioinf.uni-greifswald.de/augustus/binaries/augustus-3.3.tar.gz \
&& tar -xvf augustus*.tar.gz \
&& rm augustus*.tar.gz \
&& cd augustus \
&& echo "COMPGENEPRED = true" >> common.mk \
&& echo "SQLITE = true" >> common.mk \
&& make \
&& make install

# Install ProgressiveCactus
RUN ln -s /usr/lib/python2.7/plat-*/_sysconfigdata_nd.py /usr/lib/python2.7/
RUN git clone git://github.com/glennhickey/progressiveCactus.git \
&& cd progressiveCactus \
&& git checkout tags/0.1 -b 0.1 \
&& git submodule update --init

COPY patches/ktremote.patch progressiveCactus/submodules/kyototycoon/
COPY patches/ktulog.patch progressiveCactus/submodules/kyototycoon/
COPY patches/kyotocabinet-1.2.76-gcc6.patch progressiveCactus/submodules/kyotocabinet/
RUN cd progressiveCactus/submodules/kyototycoon && patch < ktulog.patch && patch < ktremote.patch
RUN cd progressiveCactus/submodules/kyotocabinet && patch < kyotocabinet-1.2.76-gcc6.patch
RUN cd progressiveCactus && make

# Install Hisat2
RUN wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.1.0-Linux_x86_64.zip \
&& unzip hisat2-2.1.0-Linux_x86_64.zip \
&& mv hisat2-2.1.0 hisat2 \
&& rm *.zip

# Install MASH v2.0
RUN wget https://github.com/marbl/Mash/releases/download/v2.0/mash-Linux64-v2.0.tar \
&& tar -xvf mash*.tar \
&& rm mash*.tar \
&& mv mash-* mash

# Install newick utils
RUN wget http://cegg.unige.ch/pub/newick-utils-1.6-Linux-x86_64-disabled-extra.tar.gz \
&& tar -xvf newick-utils*.tar.gz \
&& rm newick-utils*.tar.gz \
&& mv newick-utils-* newick-utils \
&& cd newick-utils \
&& ./configure \
&& make

# Install CodingQuarry
RUN wget https://downloads.sourceforge.net/project/codingquarry/CodingQuarry_v2.0.tar.gz \
&& tar -xvf CodingQuarry*.tar.gz \
&& rm CodingQuarry*.tar.gz \
&& mv CodingQuarry_v2.0 codingquarry \
&& cd codingquarry \
&& make

# Install kentUtils
RUN git clone git://github.com/ENCODE-DCC/kentUtils.git \
&& cd kentUtils \
&& make

# Install blat
RUN wget http://hgwdev.cse.ucsc.edu/~kent/src/blatSrc36.zip \
&& mkdir -p /root/bin/x86_64 \
&& unzip blatSrc36.zip \
&& rm -rf blat*.zip \
&& mv blatSrc blat \
&& cd blat \
&& make

# Install Trinity v2.5.1
RUN wget https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.5.1.tar.gz \
&& tar -xvf Trinity*.tar.gz \
&& rm Trinity*.tar.gz \
&& mv trinityrnaseq-Trinity-v2.5.1 trinity
COPY patches/Chrysalis_makefile.patch /usr/local/trinity/Chrysalis/
RUN cd /usr/local/trinity/Chrysalis \
&& patch < Chrysalis_makefile.patch \
&& cd /usr/local/trinity \
&& make \
&& make plugins \
&& make install

ENV TRINITY_HOME /usr/local/bin/trinity
ENV QUARRY_PATH /usr/local/codingquarry/QuarryFiles
ENV AUGUSTUS_CONFIG_PATH /usr/local/augustus/config
ENV PYTHONPATH /usr/local/progressiveCactus/submodules
ENV PATH /usr/local/augustus/bin:/usr/local/augustus/scripts:/usr/local/progressiveCactus/bin:/usr/local/progressiveCactus/submodules/kentToolBinaries:/usr/local/hisat2:/usr/local/mash:/usr/local/progressiveCactus/submodules/hal/bin:/usr/local/newick-utils/src:/usr/local/codingquarry:/usr/local/kentUtils/bin:/root/bin/x86_64:/usr/local/bin/trinity:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
