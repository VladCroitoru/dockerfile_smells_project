FROM ubuntu:16.04 as builder

RUN apt-get update && \
    apt-get install -y git curl unzip build-essential fasm libboost-dev libboost-system-dev libboost-log-dev libboost-thread-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

RUN curl -LOs https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh && \
    chmod +x cmake-3.10.2-Linux-x86_64.sh && \
    ./cmake-3.10.2-Linux-x86_64.sh --skip-license --prefix=/usr/local && \
    rm cmake-3.10.2-Linux-x86_64.sh

RUN curl -LOs https://github.com/dmikushin/nheqminer/archive/master.zip && \
    unzip master.zip && \
    rm master.zip && \
    cd nheqminer-master && \
    mkdir build && \
    cd build && \
    cmake -DUSE_CUDA_DJEZO=off .. && \
    make -j$(nproc)

FROM ubuntu:16.04

COPY --from=builder /tmp/nheqminer-master/build/nheqminer /usr/bin
ENTRYPOINT ["/usr/bin/nheqminer"]
