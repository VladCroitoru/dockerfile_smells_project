FROM ubuntu:16.04
MAINTAINER Jonathan Creekmore <jonathan@thecreekmores.org>

ENV DEBIAN_FRONTEND=noninteractive
ENV USER root

# build depends
RUN apt-get update && \
    apt-get --quiet --yes install \
        build-essential curl pkg-config git \
        apt-transport-https && \
        apt-get autoremove -y && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*

# install rustup
RUN curl https://sh.rustup.rs -sSf > rustup-install.sh && \
    sh ./rustup-install.sh -y --default-toolchain 1.20-x86_64-unknown-linux-gnu && \
    rm rustup-install.sh

# Install Rust nightly
RUN /root/.cargo/bin/rustup toolchain install nightly-2017-09-13-x86_64-unknown-linux-gnu

# Install clippy
RUN /root/.cargo/bin/rustup run nightly-2017-09-13 -- cargo install --root /usr/local clippy --vers 0.0.160


RUN mkdir /source
VOLUME ["/source"]
WORKDIR /source

CMD ["/bin/bash"]
