FROM ubuntu:16.04

### File author / maintainer
MAINTAINER Olivier Harismendy "oharismendy@ucsd.edu"

### change a working directory to /opt #######
WORKDIR /opt

### install
RUN apt-get update && apt-get install -y \
autoconf \
build-essential \
curl \
git \
g++ \
libncurses5-dev \
libssl-dev \
libboost-all-dev \
libbz2-dev \
make \
man \
pkg-config \
python \
python-tk \
python-pip \
python-dev \
python-numpy \
python-yaml \
software-properties-common \
screen \
vim \
wget \
zip \
zlibc \
zlib1g \
zlib1g-dev \
gedit \
gpicview \
r-base \
perl \
gzip

RUN R -e "install.packages(c('heatmap.2','ggplot2','reshape2','dplyr','plyr'), repos = 'http://cran.rstudio.com/')" 

RUN pip install --upgrade pip &&\
    pip install weblogo 
    
RUN apt-get install -y \
samtools \
bedtools

RUN git clone https://github.com/lh3/bwa.git && \
	cd bwa && \
	make &&\
  	cp bwa /usr/local/bin

RUN git clone https://github.com/oharismendy/PipeDuct.git &&\
	mkdir -p /scratch &&\
	chmod -R 755 /opt/PipeDuct
	
ENV PATH="/opt/PipeDuct/:${PATH}" 
	
WORKDIR /scratch
