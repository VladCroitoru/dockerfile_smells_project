# based-on Ubuntu-18.04 (bionic)
FROM ubuntu:bionic

ARG DEBIAN_FRONTEND="noninteractive" 
ENV TZ="America/New_York"

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install  locales -y
RUN rm -rf /var/lib/apt/lists/*
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

RUN apt-get update -y

#install the required packages
RUN apt-get install wget curl git python python3 openjdk-8-jdk openjdk-11-jdk ant autoconf bison pkg-config zip unzip build-essential gettext gcc-multilib libx11-dev libxext-dev libxrender-dev libxtst-dev libxt-dev libcups2-dev libasound2-dev libfontconfig1-dev libtool -y && apt-get clean

# get rust toolchain version
RUN wget https://raw.githubusercontent.com/mmtk/mmtk-core/master/rust-toolchain

# install rustup without any default toolchain
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain none -y
RUN /bin/sh -c ". /root/.cargo/env"

# install our current rust toolchain and std library
# NOTE: ensure to set the RUSTUP_TOOLCHAIN environment variable
RUN export RUSTUP_TOOLCHAIN=$(cat rust-toolchain) && /root/.cargo/bin/rustup toolchain install $RUSTUP_TOOLCHAIN
RUN export RUSTUP_TOOLCHAIN=$(cat rust-toolchain) && /root/.cargo/bin/rustup target add i686-unknown-linux-gnu --toolchain $RUSTUP_TOOLCHAIN

# Add .cargo/bin to PATH
ENV PATH="/root/.cargo/bin:${PATH}"

ENV HOME /root
WORKDIR /root

CMD ["bash", "--login"]
