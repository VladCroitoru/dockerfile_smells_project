FROM debian:latest
MAINTAINER Niema Moshiri <niemamoshiri@gmail.com>
RUN apt-get update && apt-get -y upgrade

# set up pypy first to avoid conflicts
RUN apt-get install -y pypy curl unzip
RUN curl -O https://pypi.python.org/packages/72/c2/c09362ab29338413ab687b47dab03bab4a792e2bbb727a1eb5e0a88e3b86/setuptools-39.0.1.zip && unzip setuptools-39.0.1.zip
RUN cd setuptools-39.0.1 && pypy bootstrap.py && pypy setup.py install
RUN cd ..
RUN curl https://pypi.python.org/packages/e0/69/983a8e47d3dfb51e1463c1e962b2ccd1d74ec4e236e232625e353d830ed2/pip-10.0.0.tar.gz | tar -zx
RUN cd pip-10.0.0 && pypy setup.py install
RUN cd ..
RUN curl https://pypi.python.org/packages/5d/c1/45947333669b31bc6b4933308dd07c2aa2fedcec0a95b14eedae993bd449/wheel-0.31.0.tar.gz | tar -zx
RUN cd wheel-0.31.0 && pypy setup.py install
RUN cd ..
RUN for f in easy_install easy_install-2.7 pip pip2 pip2.7; do mv /usr/local/bin/$f /usr/local/bin/pypy-$f; done
RUN rm -rf setuptools* pip-10.0.0 wheel-0.31.0

# install all other dependencies
RUN apt-get install -y autoconf automake bzip2 cmake curl cython default-jre default-jre-headless gcc git g++ htop less libboost-all-dev libbz2-dev libcrypto++-dev libcurl3-dev libgomp1 libhdf5-dev libkrb5-dev liblzma-dev libncurses5-dev libssl-dev libtbb-dev libz-dev make man-db openjdk-8-jre openjdk-8-jre-headless parallel perl pigz pkg-config python python-pip python3 python3-biopython python3-numpy python3-pip python3-scipy python3-setuptools python3-six python3-tornado rsync unzip wget zlib1g zlib1g-dev

# BCFtools
RUN wget -qO- https://github.com/samtools/bcftools/releases/download/1.8/bcftools-1.8.tar.bz2 | tar -jx
RUN cd bcftools-1.8 && ./configure --prefix=/usr/local && make && make install
RUN cd ..
RUN rm -rf bcftools-1.8

# BEAST 2.5.0
RUN wget -qO- https://github.com/CompEvol/beast2/releases/download/v2.5.0/BEAST.v2.5.0.Linux.tgz | tar -zx
RUN mv beast /usr/local/bin/beast_files && ln -s /usr/local/bin/beast_files/bin/* /usr/local/bin

# bedtools
RUN apt-get install -y bedtools

# Bowtie
RUN apt-get install -y bowtie

# Bowtie2
RUN apt-get install -y bowtie2

# BWA
RUN git clone https://github.com/lh3/bwa.git
RUN cd bwa && make && mv bwa /usr/local/bin && mkdir -p /usr/local/share/man/man1 && mv bwa.1 /usr/local/share/man/man1
RUN cd ..
RUN rm -rf bwa

# Cufflinks
RUN curl -s http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz | tar -zx
RUN rm cufflinks-2.2.1.Linux_x86_64/AUTHORS cufflinks-2.2.1.Linux_x86_64/LICENSE cufflinks-2.2.1.Linux_x86_64/README
RUN mv cufflinks-2.2.1.Linux_x86_64/* /usr/local/bin
RUN rm -rf cufflinks-2.2.1.Linux_x86_64

# FastQC
RUN apt-get install -y fastqc

# FastTree
RUN curl http://www.microbesonline.org/fasttree/FastTree.c > FastTree.c
RUN gcc -DUSE_DOUBLE -DOPENMP -fopenmp -O3 -finline-functions -funroll-loops -Wall -o FastTree FastTree.c -lm
RUN mv FastTree /usr/local/bin && rm FastTree.c

# HIV-TRACE
RUN git clone https://github.com/veg/tn93.git && cd tn93 && cmake ./ && make install
RUN cd ..
RUN pip3 install hivtrace
RUN rm -rf tn93

# HMMER
RUN apt-get install -y hmmer

# MAFFT
RUN apt-get install -y mafft

# MrBayes
RUN apt-get install -y mrbayes

# PASTA
RUN cd /usr/local/bin
RUN git clone https://github.com/smirarab/pasta.git
RUN git clone https://github.com/smirarab/sate-tools-linux.git
RUN cd sate-tools-linux && git checkout d78ef029b533e4f4ac13ba1e9cfdac7944b1f70e && cd ..
RUN cd pasta && python3 setup.py develop
RUN rm /usr/local/bin/run_pasta_gui.py
RUN cd
ENV CONTRALIGN_DIR /usr/local/bin/sate-tools-linux

# pgltools
RUN pypy-pip install PyGLtools
RUN git clone https://github.com/billgreenwald/pgltools.git && mv pgltools /usr/local/bin/pgltools_files && ln -s /usr/local/bin/pgltools_files/sh/pgltools /usr/local/bin/pgltools

# RAxML
RUN apt-get install -y raxml

# SAMtools
RUN wget -qO- https://github.com/samtools/samtools/releases/download/1.8/samtools-1.8.tar.bz2 | tar -jx
RUN cd samtools-1.8 && ./configure --prefix=/usr/local && make && make install
RUN cd ..
RUN rm -rf samtools-1.8

# Seq-Gen
RUN wget -qO- https://github.com/rambaut/Seq-Gen/archive/1.3.4.tar.gz | tar -zx
RUN cd Seq-Gen-1.3.4/source && make && mv seq-gen /usr/local/bin
RUN cd ../..
RUN rm -rf Seq-Gen-1.3.4

# SPAdes
RUN curl -s http://cab.spbu.ru/files/release3.11.1/SPAdes-3.11.1-Linux.tar.gz | tar -zx
RUN mv SPAdes-3.11.1-Linux/bin/* /usr/local/bin && mv SPAdes-3.11.1-Linux/share/* /usr/local/share
RUN rm -rf SPAdes-3.11.1-Linux

# STAR
RUN apt-get install -y rna-star

# TopHat
RUN apt-get install -y tophat

# Trimmomatic
RUN apt-get install -y trimmomatic

# UCSC Genome Browser Utilities
RUN rsync -aP rsync://hgdownload.soe.ucsc.edu/genome/admin/exe/linux.x86_64/ /usr/local/bin

# VCFtools
RUN apt-get install -y vcftools

# clean up
RUN mandb && apt-get clean

# useful aliases
RUN echo 'alias ll="ls -l"' >> ~/.bashrc
RUN echo 'alias llh="ls -lh"' >> ~/.bashrc
RUN echo 'alias lla="ls -la"' >> ~/.bashrc
