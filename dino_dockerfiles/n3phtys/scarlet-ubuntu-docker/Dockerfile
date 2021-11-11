FROM ubuntu:18.04

RUN mkdir /root/build && cd /root/build/ \
  && apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y build-essential ssh git cmake libgmp-dev llvm clang lib32z1-dev \
  && apt-get install -y libllvm5.0 clang-5.0 llvm-5.0 llvm-5.0-dev llvm-5.0-runtime llvm-5.0-tools
