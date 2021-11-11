FROM ubuntu:latest
RUN \
apt-get update && apt-get install -y \
wget \
build-essential \
libxslt-dev \
libxml2-dev

ENV SRC /opt
ENV BIN /usr/local/bin

WORKDIR $SRC

RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/1.2.0/ncbi-magicblast-1.2.0-x64-linux.tar.gz && \
	tar -xzvf ncbi-magicblast-1.2.0-x64-linux.tar.gz && \
	cd ncbi-magicblast-1.2.0/bin/ && \
	wget https://helix.nih.gov/~tsang/magicblast13 && \
	chmod 777 magicblast13 && \
	cp -rf  *  $BIN

COPY Dockerfile /opt/Dockerfile
