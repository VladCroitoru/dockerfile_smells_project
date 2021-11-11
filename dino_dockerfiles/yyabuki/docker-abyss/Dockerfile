FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# a bit modified Michael Barton's Dockerfile and run files

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y libsparsehash-dev libboost-all-dev openmpi-bin gcc make autoconf bsdmainutils r-base-core python && \
    apt-get clean && \
    rm -r /var/lib/apt/lists/*

ADD http://kmergenie.bx.psu.edu/kmergenie-1.6741.tar.gz /tmp/kmergenie.tar.gz
RUN mkdir /tmp/kmergenie
RUN tar xzf /tmp/kmergenie.tar.gz --directory /tmp/kmergenie --strip-components=1
RUN cd /tmp/kmergenie && make && make install

ADD https://github.com/bcgsc/abyss/releases/download/1.5.2/abyss-1.5.2.tar.gz /tmp/abyss.tar.gz
RUN mkdir /tmp/abyss
RUN tar xzf /tmp/abyss.tar.gz --directory /tmp/abyss --strip-components=1

# See https://github.com/bcgsc/abyss/wiki/ABySS-Users-FAQ
RUN cd /tmp/abyss && \
       ./configure --enable-maxk=128 && \
       make && \
       make install

ADD run /usr/local/bin/
ADD estimate_kmer /usr/local/bin/
ADD Procfile /

ENTRYPOINT ["run"]
