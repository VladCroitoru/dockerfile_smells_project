FROM    ubuntu:14.04

MAINTAINER  keiranmraine@gmail.com

LABEL   uk.ac.sanger.cgp="Cancer Genome Project, Wellcome Trust Sanger Institute" \
        version="0.0" \
        description="The CGP somatic calling pipeline 'in-a-box'"

USER    root

RUN     mkdir /tmp/downloads && \
        apt-get -yqq update && \
        apt-get -yqq install build-essential autoconf software-properties-common python-software-properties \
          wget curl rsync nano zlib1g-dev libncurses5-dev libgd-dev \
          libgd2-xpm-dev libexpat1-dev python unzip libboost-dev libboost-iostreams-dev \
          libpstreams-dev libglib2.0-dev && \
        apt-get clean

WORKDIR /tmp/downloads
# PCAP-core
RUN     curl -sSL https://github.com/ICGC-TCGA-PanCancer/PCAP-core/archive/v1.12.1.tar.gz | tar xz && \
        cd /tmp/downloads/PCAP-core-1.12.1 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm


# cgpVcf
RUN     curl -sSL https://github.com/cancerit/cgpVcf/archive/v1.3.1.tar.gz | tar xz && \
        cd /tmp/downloads/cgpVcf-1.3.1 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# cgpPindel
RUN     curl -sSL https://github.com/cancerit/cgpPindel/archive/v1.5.4.tar.gz | tar xz && \
        cd /tmp/downloads/cgpPindel-1.5.4 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# alleleCount
RUN     curl -sSL https://github.com/cancerit/alleleCount/archive/v2.1.2.tar.gz | tar xz && \
        cd /tmp/downloads/alleleCount-2.1.2 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# ascatNgs
RUN     curl -sSL https://github.com/cancerit/ascatNgs/archive/v1.5.2.tar.gz | tar xz && \
        cd /tmp/downloads/ascatNgs-1.5.2 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# cgpCaVEManPostProcessing
RUN     curl -sSL https://github.com/cancerit/cgpCaVEManPostProcessing/archive/1.5.1.tar.gz | tar xz && \
        cd /tmp/downloads/cgpCaVEManPostProcessing-1.5.1 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# cgpCaVEManWrapper
RUN     curl -sSL https://github.com/cancerit/cgpCaVEManWrapper/archive/1.9.0.tar.gz | tar xz && \
        cd /tmp/downloads/cgpCaVEManWrapper-1.9.0 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm ~/.cache

# VAGrENT
RUN     curl -sSL https://github.com/cancerit/VAGrENT/archive/v2.1.2.tar.gz | tar xz && \
        cd /tmp/downloads/VAGrENT-2.1.2 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# grass
RUN     curl -sSL https://github.com/cancerit/grass/archive/v1.1.6.tar.gz | tar xz && \
        cd /tmp/downloads/grass-1.1.6 &&./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm

# fasta36 dependancy of BRASS
RUN     curl -sSL https://github.com/wrpearson/fasta36/archive/v36.3.8.tar.gz | tar xz && \
        cd /tmp/downloads/fasta36-36.3.8/src && make -f ../make/Makefile.linux64 install XDIR=/opt/wtsi-cgp/bin && cd /tmp/downloads && rm -rf *

# BRASS deps
RUN     echo 'deb http://cran.rstudio.com/bin/linux/ubuntu trusty/' >> /etc/apt/sources.list && \
        apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
        add-apt-repository -y ppa:marutter/rdev && \
        apt-get -yqq update && \
        apt-get -yqq upgrade && \
        apt-get -mqy install python unzip libboost-dev libboost-iostreams-dev libpstreams-dev libglib2.0-dev \
          r-base r-base-core r-cran-rcolorbrewer r-cran-gam r-cran-VGAM r-cran-stringr && \
        apt-get clean

# BRASS Bioconductor packages not available via apt-get:
COPY    bioconductor.R /tmp/downloads/bioconductor.R
RUN     Rscript /tmp/downloads/bioconductor.R && rm -f /tmp/downloads/bioconductor.R

# BRASS
RUN     curl -sSL https://github.com/cancerit/BRASS/archive/v4.0.12.tar.gz | tar xz && \
        cd /tmp/downloads/BRASS-4.0.12 && ./setup.sh /opt/wtsi-cgp && cd /tmp/downloads && rm -rf * && rm -rf ~/.cpanm


## USER CONFIGURATION
RUN     useradd -ms /bin/bash cgpbox
USER    newuser
WORKDIR /home/newuser
