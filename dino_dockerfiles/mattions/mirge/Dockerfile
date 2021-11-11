# miRge - a rational and efficient approach to miRNA-seq

# base image from ubuntu
FROM ubuntu

WORKDIR /opt

RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    libgd-graph-perl \
    libhtml-table-perl \
    python-setuptools \
    python-dev \
    unzip \
    wget \
    git \
    python-pip \
 	&& rm -rf /var/lib/apt/lists/*

# Dependecies needed:
# 1. Cutadapt

RUN pip install cutadapt

# 2. Bowtie 

RUN wget http://sourceforge.net/projects/bowtie-bio/files/bowtie/1.1.1/bowtie-1.1.1-linux-x86_64.zip/download -O bowtie-1.1.1-linux-x86_64.zip
RUN unzip bowtie-1.1.1-linux-x86_64.zip
ENV PATH /opt/bowtie-1.1.1:$PATH

# 3. Clone miRge and get the Libraries used by the software

RUN git clone https://github.com/BarasLab/miRge.git

RUN wget --quiet http://atlas.pathology.jhu.edu/baras/miRge/miRge.seqLibs.tar.gz && \
	tar -zxvf miRge.seqLibs.tar.gz && \
	mv usr/local/miRge/* /opt/miRge/ && \
	rm miRge.seqLibs.tar.gz
	


