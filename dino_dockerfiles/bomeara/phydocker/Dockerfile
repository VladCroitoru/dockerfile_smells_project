FROM rocker/rstudio:latest

MAINTAINER Brian O'Meara <omeara.brian@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update

RUN apt-get install -y apt-utils

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    libxss1 \
    libxt6 \
    libxext6 \
    libsm6 \
    libice6 \
    xdg-utils \
    libxml2-dev \
    xorg \
    libx11-dev \
    libglu1-mesa-dev \
    libfreetype6-dev \
    libmagick++-dev \
	libudunits2-dev \
	libfftw3-dev \
	libgsl-dev \
	libgit2-dev \
	libharfbuzz-dev \
	libfribidi-dev \
	libgdal-dev \ 
  && rm -rf /var/lib/apt/lists/*

RUN apt-get update

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    echo keyboard-configuration keyboard-configuration/layout select 'English (US)' | debconf-set-selections && \
    echo keyboard-configuration keyboard-configuration/layoutcode select 'us' | debconf-set-selections && \
    echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-selections

RUN echo 'options(repos = c(CRAN="https://cran.rstudio.com"))' > ~/.Rprofile

# RUN apt-get install -y software-properties-common

RUN apt-get -y install python-dev

RUN apt-get -y install libcgal-dev libglu1-mesa-dev libglu1-mesa-dev libx11-dev

RUN apt-get update

RUN apt-get -y install x11-common

RUN apt-get install -y libmpfr-dev libmpfr-doc

RUN apt-get install -y curl

RUN apt-get install libgl1-mesa-dev

RUN apt-get install ed

RUN apt-get install -y mafft

RUN apt-get install -y muscle

# RUN apt-get install -y python-numpy

# RUN apt-get install -y python-scipy

# RUN apt-get install -y python-biopython

# RUN apt-get install dnsutils -y

# RUN apt-get install -y python3-pip

# RUN python3 -m pip install git+https://github.com/jeetsukumaran/DendroPy.git

# RUN apt-get install -y puppet

RUN Rscript -e "install.packages('ctv', dependencies=TRUE)"

RUN Rscript -e "install.packages('devtools', dependencies=TRUE)"

RUN Rscript -e "ctv::install.views('Phylogenetics')"

RUN Rscript -e "install.packages('hisse', dependencies=TRUE)"

RUN Rscript -e "install.packages('diagram')"

# RUN Rscript -e "devtools::install_github('cran/P2C2M')"

# RUN Rscript -e "devtools::install_github('bomeara/phrapl')"

# RUN Rscript -e "devtools::install_github( 'heibl/ips')"

# RUN Rscript -e 'source("https://bioconductor.org/biocLite.R")'

RUN Rscript -e "install.packages('tidyverse')"

RUN Rscript -e "install.packages('drake')"

RUN mkdir /usr/local/pathd8download && \
wget http://www2.math.su.se/PATHd8/PATHd8.zip -O /usr/local/pathd8download/PATHd8.zip && \
cd /usr/local/pathd8download && \
unzip /usr/local/pathd8download/PATHd8.zip && \
cc PATHd8.c -O3 -lm -o PATHd8 && \
cp PATHd8 /usr/local/bin/PATHd8

# RUN mkdir /usr/local/supersmart && \
# cd /usr/local/supersmart && \
# git clone https://github.com/naturalis/supersmart.git && \
# cd supersmart/conf && \
# puppet apply


# From https://github.com/Linuxbrew/docker/blob/master/centos7/Dockerfile

RUN apt-get install -y curl make ruby sudo \
  && apt-get clean all


RUN apt-get install -y raxml

# RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \
# 	&& useradd -m -s /bin/bash linuxbrew \
# 	&& echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers

# USER linuxbrew
# WORKDIR /home/linuxbrew

# ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH \
# 	SHELL=/bin/bash \
# 	USER=linuxbrew

# RUN yes | ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)" \
# 	&& brew config


# RUN brew tap jonchang/biology

# # RUN brew tap brewsci/bio

# RUN brew install revbayes

# RUN brew install bucky

# # RUN brew tap bomeara/homebrew-science


# RUN brew install phylip

# RUN brew install raxml

# RUN brew install pandoc


# RUN brew install phlawd

# # RUN brew install phylocom

# RUN brew install beast

# RUN brew install brewsci/bio/beast2

# RUN brew install brewsci/bio/exonerate

# RUN brew install brewsci/bio/prank

# RUN brew install brewsci/bio/raxml


# RUN brew install brewsci/bio/trimal

# RUN brew install brewsci/bio/clustal-omega

# RUN brew install brewsci/bio/fasttree

# RUN brew install bomeara/science/raxml

# RUN brew install bomeara/science/phylip

# RUN brew install bomeara/science/phyutility


#RUN cp /home/linuxbrew/.linuxbrew/bin/raxmlHPC-PTHREADS /home/linuxbrew/.linuxbrew/bin/raxml

# RUN cp /home/linuxbrew/.linuxbrew/bin/raxmlHPC-PTHREADS /home/linuxbrew/.linuxbrew/bin/raxmlHPC

USER root

RUN Rscript -e "install.packages('knitr')"

RUN Rscript -e "install.packages('bookdown')"


# ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH


RUN localedef -i en_US -f UTF-8 en_US.UTF-8 \
	&& useradd -m -s /bin/bash linuxbrew \
	&& echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers


USER linuxbrew
WORKDIR /home/linuxbrew


RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

RUN test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
RUN test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
RUN test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
RUN echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile

RUN brew install brewsci/bio/treepl

RUN brew install brewsci/bio/beast2

RUN brew install bomeara/science/phyutility

RUN brew install brewsci/bio/clustal-omega

RUN brew install brewsci/bio/phlawd

#RUN mkdir /usr/local/phylocom && \
#wget https://github.com/downloads/phylocom/phylocom/phylocom-4.2.zip -O /usr/local/phylocom/phylocom.zip && \
#cd /usr/local/phylocom && \
#unzip /usr/local/phylocom/phylocom.zip && \
#cd /usr/local/phylocom/phylocom-4.2/src && \
#make && \
#cp phylocom /usr/local/bin && \
#cp phylomatic /usr/local/bin


#RUN mkdir /usr/local/paup
#RUN wget http://phylosolutions.com/paup-test/paup4a166_ubuntu64.gz -O /usr/local/paup/paup.gz
#RUN cd /usr/local/paup
#RUN gunzip /usr/local/paup/paup.gz
#RUN chmod u+x /usr/local/paup/paup
#RUN cp /usr/local/paup/paup /usr/local/bin/paup
