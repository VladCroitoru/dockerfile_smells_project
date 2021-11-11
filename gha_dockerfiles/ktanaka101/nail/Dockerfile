FROM rust:slim-bullseye AS base

RUN apt-get update && apt-get -y upgrade

# See: https://apt.llvm.org/
RUN apt-get install -y gnupg2
RUN apt-get install -y wget

RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -

RUN echo 'deb http://apt.llvm.org/bullseye/ llvm-toolchain-bullseye-11 main' >> /etc/apt/sources.list

RUN apt-get update

# LLVM
RUN apt-get install -y libllvm-11-ocaml-dev libllvm11 llvm-11 llvm-11-dev llvm-11-doc llvm-11-examples llvm-11-runtime
# Clang and co
# Replaced python-clang-10 to python3-clang-10
RUN apt-get install -y clang-11 clang-tools-11 clang-11-doc libclang-common-11-dev libclang-11-dev libclang1-11 clang-format-11 python3-clang-11 clangd-11
# libfuzzer
RUN apt-get install -y libfuzzer-11-dev
# lldb
RUN apt-get install -y lldb-11
# lld (linker)
RUN apt-get install -y lld-11
# libc++
RUN apt-get install -y libc++-11-dev libc++abi-11-dev
# OpenMP
RUN apt-get install -y libomp-11-dev

# Building error for rust: note: /usr/bin/ld: cannot find -lz
# Required zlib1g-dev
RUN apt install -y zlib1g-dev

ENV PATH $PATH:/usr/lib/llvm-11/bin/

# fast build by the rust in docker
ENV CARGO_BUILD_TARGET_DIR=/tmp/target

# llvm
ENV LLVM_SYS_111_STRICT_VERSIONING=111
ENV LLVM_SYS_111_PREFIX=/usr/lib/llvm-11


# for development
FROM base AS development

RUN apt-get install -y git
RUN rustup component add rustfmt clippy rls rust-analysis rust-src

# for CI
FROM base AS ci

RUN rustup component add rustfmt clippy