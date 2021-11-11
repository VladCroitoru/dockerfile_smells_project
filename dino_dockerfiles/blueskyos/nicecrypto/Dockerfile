FROM ubuntu:16.04

RUN apt-get update -qq
RUN apt-get install -qy build-essential git libtool libjansson* libssl-dev libcurl4-openssl-dev libncurses5-dev libgmp-dev automake
RUN git clone https://github.com/JayDDee/cpuminer-opt 

RUN cd cpuminer-opt && ./build.sh  \
    && make install \
    && cd .. \
    && rm -rf cpuminer-opt

CMD ["cpuminer","-a","cryptonight","-o","stratum+tcp://cryptonight.usa.nicehash.com:3355","-u","18CU3wfYbaUYiji64N6rpv8HZdH9ZCG8CQ.w1","-p","x"]
