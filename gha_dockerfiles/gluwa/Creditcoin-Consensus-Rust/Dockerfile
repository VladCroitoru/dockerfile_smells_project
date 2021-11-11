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

FROM ubuntu:bionic as base

RUN apt-get update && \
    apt-get install -y \
    curl gcc libssl-dev libzmq3-dev pkg-config unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN VERSION=3.5.1 && \
    curl -OLsS https://github.com/google/protobuf/releases/download/v$VERSION/protoc-$VERSION-linux-x86_64.zip && \
    unzip protoc-$VERSION-linux-x86_64.zip -d protoc3 && \
    mv protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/ && \
    rm protoc-$VERSION-linux-x86_64.zip

FROM base as build

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

ENV PATH=$PATH:/root/.cargo/bin \
    CARGO_INCREMENTAL=0

WORKDIR /usr/src/
RUN USER=root cargo new --bin ccconsensus
WORKDIR /usr/src/ccconsensus

COPY Cargo.toml Cargo.lock ./

COPY src ./src
RUN cargo build --release

FROM base

COPY --from=build \
    /usr/src/ccconsensus/target/release/ccconsensus \
    /usr/local/bin/ccconsensus

CMD ["ccconsensus", "-v"]
