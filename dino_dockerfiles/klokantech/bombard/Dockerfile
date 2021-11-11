FROM debian:jessie

RUN apt-get update && apt-get install -qq -y \
	libgd-graph-perl \
	wget \
	build-essential \
	automake \
	libssl-dev \
	git
RUN wget --no-verbose  http://www.cpan.org/authors/id/C/CH/CHARTGRP/Chart-2.4.6.tar.gz && tar zxf Chart-2.4.6.tar.gz && cd Chart-2.4.6 && perl Makefile.PL && make && make test && make install
RUN cd .. && git clone https://github.com/JoeDog/siege.git && cd siege && utils/bootstrap && ./configure && make && make install

# Siege must be installed before bombard, as bombard determines siege's path at build time
RUN git clone https://github.com/allardhoeve/bombard.git && cd bombard && ./configure && make && make install

COPY .siegerc /root/.siegerc
