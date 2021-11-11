FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install locales

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install dependencies
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update

# General things
RUN apt-get install -qq wget unzip build-essential cmake gcc libcunit1-dev libudev-dev

RUN apt-get install -qq  libcurl4-gnutls-dev

# Python things
RUN apt-get install -y python3 python3-dev python3-pip r-base

# Canu things
RUN apt-get install -y default-jre gnuplot

RUN pip3 install jupyter

# Grab the checked out source
RUN mkdir -p /work
WORKDIR /work

# Install canu
RUN wget https://github.com/marbl/canu/releases/download/v1.7/canu-1.7.Linux-amd64.tar.xz
RUN tar -xvf canu-1.7.Linux-amd64.tar.xz

# Install blast plus
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.7.1+-x64-linux.tar.gz
RUN tar -zxvf ncbi-blast-2.7.1+-x64-linux.tar.gz

# it needs perl-doc
RUN apt-get install -qq perl-doc

# Download some blast databases
# RUN ncbi-blast-2.7.1+/bin/update_blastdb.pl nr nt

# Install more pythons
RUN apt-get install -qq python-pip

# Install poretools
RUN pip install poretools

# Make viz
RUN pip install matplotlib scikit-learn

# Do BAM things
RUN pip install pysam

# Get MetaGeneMark

RUN wget http://topaz.gatech.edu/GeneMark/tmp/GMtool_H80a6/MetaGeneMark_linux_64.tar.gz
RUN tar -zvxf MetaGeneMark_linux_64.tar.gz
RUN cp MetaGeneMark_linux_64/mgm/gmhmmp /usr/bin/.


WORKDIR /root
RUN wget http://topaz.gatech.edu/GeneMark/tmp/GMtool_H80a6/gm_key_64.gz
RUN gunzip gm_key_64.gz
RUN mv gm_key_64 .gm_key

WORKDIR /work

# Get mash
RUN wget https://github.com/marbl/Mash/releases/download/v2.0/mash-Linux64-v2.0.tar
RUN tar -xvf mash-Linux64-v2.0.tar
RUN cp mash-Linux64-v2.0/mash /usr/bin/.

# Get git
RUN apt-get install -qq git

# Get miniasm
RUN git clone https://github.com/lh3/miniasm.git
WORKDIR /work/miniasm
RUN make
RUN cp miniasm /usr/bin/.
RUN cp minidot /usr/bin/.

WORKDIR /work

# Get minimap2
RUN git clone https://github.com/lh3/minimap2.git

WORKDIR /work/minimap2
RUN make
RUN cp minimap2 /usr/bin/.

# Get BioPython
RUN pip3 install biopython


WORKDIR /work

RUN git clone https://github.com/NCBI-Hackathons/SpoonFedNanopore.git
RUN cp -R SpoonFedNanopore/* .


CMD ["/usr/local/bin/jupyter", "notebook", "--port", "8888", "--ip", "0.0.0.0", "--allow-root"]
