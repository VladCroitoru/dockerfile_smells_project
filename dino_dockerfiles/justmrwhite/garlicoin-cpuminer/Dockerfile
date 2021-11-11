FROM ubuntu

RUN apt-get update && apt-get install -y \
    git \
    automake autoconf pkg-config libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev make g++

RUN git clone https://github.com/tpruvot/cpuminer-multi

WORKDIR /cpuminer-multi 

RUN ./build.sh
