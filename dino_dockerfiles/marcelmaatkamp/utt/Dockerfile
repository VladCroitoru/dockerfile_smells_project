FROM ubuntu:17.04
EXPOSE 1883
RUN deps='software-properties-common' && \
    apt-get update && \
    apt-get install -y --no-install-recommends $deps && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get install -y gcc-7 g++-7 --no-install-recommends && \
    apt-get install -y git make && \
    apt-get purge -y --auto-remove $deps && \
    rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN git clone --recursive https://github.com/uNetworking/uTT.git
WORKDIR uTT/
RUN g++-7 -std=c++17 -O3 -s -I. src/*.cpp uSockets/Berkeley.cpp uSockets/Epoll.cpp -o uTT

ENTRYPOINT ["./uTT"]  