FROM ubuntu:14.04

WORKDIR /opt

RUN apt-get update && apt-get install -y \
	autoconf \
	automake \
	make \
	g++ \
	gcc \
	build-essential \ 
	zlib1g-dev \
	libgsl0-dev \
	perl \
	curl \
	git \
	wget \
	unzip \
	tabix \
	libncurses5-dev

RUN wget https://github.com/ldc-developers/ldc/releases/download/v0.17.1/ldc2-0.17.1-linux-x86_64.tar.xz && \
  tar xJf ldc2-0.17.1-linux-x86_64.tar.xz

ENV PATH=/opt/ldc2-0.17.1-linux-x86_64/bin/:$PATH
ENV LIBRARY_PATH=/opt/ldc2-0.17.1-linux-x86_64/lib/

RUN git clone --recursive https://github.com/lomereiter/sambamba.git && \ 
  cd sambamba; make sambamba-ldmd2-64
