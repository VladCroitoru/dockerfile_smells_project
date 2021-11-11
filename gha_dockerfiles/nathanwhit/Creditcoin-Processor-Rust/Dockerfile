#
#    Copyright(c) 2021 Gluwa, Inc.
#
#    This file is part of Creditcoin.
#
#    Creditcoin is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with Creditcoin. If not, see <https://www.gnu.org/licenses/>.
#

FROM ubuntu:bionic

RUN apt-get update \
 && apt-get install -y \
 curl \
 gcc \
 pkg-config \
 make \
 cmake \
 libssl-dev \
 automake \
 autoconf \
 unzip

# For Building Protobufs
RUN curl -OLsS https://github.com/google/protobuf/releases/download/v3.5.1/protoc-3.5.1-linux-x86_64.zip \
 && unzip protoc-3.5.1-linux-x86_64.zip -d protoc3 \
 && rm protoc-3.5.1-linux-x86_64.zip

RUN curl https://sh.rustup.rs -sSf > /usr/bin/rustup-init \
 && chmod +x /usr/bin/rustup-init \
 && rustup-init -y

ENV PATH=$PATH:/protoc3/bin:/root/.cargo/bin \
    CARGO_INCREMENTAL=0

WORKDIR /ccprocessor-rust

COPY . /ccprocessor-rust

RUN cd /ccprocessor-rust \
 && echo "\033[0;32m--- Building ccprocessor-rust ---\n\033[0m" \
 && rm -rf ./bin/ \
 && mkdir -p ./bin/ \
 && cargo build --release \
 && cp ./target/release/ccprocessor-rust ./bin/ccprocessor-rust \
 && cargo build --release --features 'old-sawtooth' \
 && cp ./target/release/ccprocessor-rust ./bin/ccprocessor-rust-1.7
