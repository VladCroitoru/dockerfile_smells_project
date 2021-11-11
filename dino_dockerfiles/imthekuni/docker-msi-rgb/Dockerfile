FROM phusion/baseimage

RUN apt-get update && apt-get install -y gcc make curl git

RUN curl https://sh.rustup.rs -sSf | \
    sh -s -- --default-toolchain stable -y

ENV PATH=/root/.cargo/bin:$PATH


RUN git clone https://github.com/nagisa/msi-rgb && cd msi-rgb && cargo build --release
