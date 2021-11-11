FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /root/snort
WORKDIR /root/snort/
#COPY ./snortrules-snapshot-3000.tar.gz ./
#COPY ./snort3-rules-3000.tar.gz ./

COPY ./snortrules-snapshot-31110.tar.gz ./

COPY ./build_snort3.sh ./
COPY ./run_snort_test_hyperscan.sh ./
COPY ./run_snort_test_ac_full.sh ./
COPY ./run_snort_test_ac_bnfa.sh ./

ENV TZ=US/LosAngeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN ./build_snort3.sh
RUN ldconfig

COPY ./build_ext.sh ./
RUN ./build_ext.sh

COPY ./maccdc2012_00001.pcap ./
#RUN /bin/bash -c "snort --help && snort -v"

