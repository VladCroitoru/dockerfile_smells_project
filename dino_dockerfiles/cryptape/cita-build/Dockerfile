FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    pkg-config \
    rabbitmq-server \
    python-pip \
    curl \
    jq \
    google-perftools \
    capnproto \
    git \
    libsnappy-dev \
    libgoogle-perftools-dev \
    libsodium* \
    libzmq3-dev \
    libssl-dev \
    binutils-dev \
    libcurl4-openssl-dev \
    zlib1g-dev \
    libdw-dev \
    libiberty-dev \
    cmake \
    build-essential \
 && curl -o v33.tar.gz -L https://github.com/SimonKagstrom/kcov/archive/v33.tar.gz \
 && tar -xf v33.tar.gz && cd kcov-33 \
 && mkdir build && cd build \
 && cmake .. && make && make install \
 && cd ../.. \
 && rm -rf v33.tar.gz kcov-33 \
 && rm -rf /var/lib/apt/lists \
 && rm -rf ~/.cache/pip


RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain nightly-2017-12-05

ENV PATH $PATH:/root/.cargo/bin

RUN cargo install --force --vers 0.3.0 rustfmt-nightly


COPY solc /usr/bin/
RUN chmod +x /usr/bin/solc

RUN pip install -U pip
RUN pip install \
    ethereum==2.2.0 \
    PyYAML==3.12 \
    jsonrpcclient==2.5.2 \
    jsonschema==2.6.0 \
    requests==2.18.4 \
    pysodium toml


COPY libgmssl.so.1.0.0 /usr/local/lib/
RUN ln -srf /usr/local/lib/libgmssl.so.1.0.0 /usr/local/lib/libgmssl.so
RUN ldconfig
