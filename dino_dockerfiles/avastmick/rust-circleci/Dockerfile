FROM debian:stretch

RUN apt-get update && \  
    apt-get install -y curl file gcc g++ git make openssh-client \
    autoconf automake cmake libtool libcurl4-openssl-dev libssl-dev \
    libelf-dev libdw-dev binutils-dev zlib1g-dev libiberty-dev wget \
    xz-utils pkg-config python

ENV KCOV_VERSION 33  
RUN wget https://github.com/SimonKagstrom/kcov/archive/v$KCOV_VERSION.tar.gz && \  
    tar xzf v$KCOV_VERSION.tar.gz && \
    rm v$KCOV_VERSION.tar.gz && \
    cd kcov-$KCOV_VERSION && \
    mkdir build && cd build && \
    cmake .. && make && make install && \
    cd ../.. && rm -rf kcov-$KCOV_VERSION

ENV PATH "$PATH:/root/.cargo/bin"  
ENV RUSTFLAGS "-C link-dead-code"  
ENV CFG_RELEASE_CHANNEL "nightly"

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    rustup update && \  
    rustup install nightly && \
    rustup default nightly && \
    rustup update nightly && \
    rustup component add rustfmt-preview --toolchain=nightly


RUN bash -l -c 'echo $(rustc --print sysroot)/lib >> /etc/ld.so.conf' && \
    bash -l -c 'echo /usr/local/lib >> /etc/ld.so.conf' && \ 
    ldconfig