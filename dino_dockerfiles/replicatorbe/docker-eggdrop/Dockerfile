FROM debian:jessie
MAINTAINER Jérôme Fafchamps (sMug [replicatorbe]) <smug@smug.fr>

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential gcc libc6 libtcl8.6 tcl8.6 tcl8.6-dev zlib1g tcllib wget unzip eggdrop-data

RUN useradd -c 'Eggdrop user' -m -d /home/eggdrop -s /bin/bash eggdrop
RUN chown -R eggdrop:eggdrop /home/eggdrop
USER eggdrop
ENV HOME /home/eggdrop
WORKDIR /home/eggdrop
RUN wget ftp://ftp.eggheads.org/pub/eggdrop/source/1.6/eggdrop1.6.21.tar.gz
RUN tar zxvf eggdrop1.6.21.tar.gz
RUN cd eggdrop1.6.21 && ./configure --with-tclinc=/usr/include/tcl8.6/tcl.h --with-tcllib=/usr/lib/x86_64-linux-gnu/libtcl8.6.so && make config && make && make install
RUN cd eggdrop && mkdir tmp