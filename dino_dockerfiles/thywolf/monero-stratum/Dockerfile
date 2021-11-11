FROM ubuntu:16.04

RUN apt-get update

RUN apt-get install git cmake build-essential libssl-dev pkg-config libboost-all-dev golang -y

RUN git clone https://github.com/monero-project/monero.git
WORKDIR /monero
RUN git checkout tags/v0.11.1.0 -b v0.11.1.0
RUN cmake -DBUILD_SHARED_LIBS=1 .
RUN make

WORKDIR /
RUN git clone https://github.com/sammy007/monero-stratum.git
WORKDIR /monero-stratum
RUN MONERO_DIR=/monero cmake .
RUN make

WORKDIR /monero-stratum

ADD config.json /monero-stratum/config.json

EXPOSE 1111
EXPOSE 3333
EXPOSE 8082

CMD ["./build/bin/monero-stratum", "config.json"]
