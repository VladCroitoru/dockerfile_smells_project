FROM ubuntu:14.04

RUN apt-get -y update
RUN apt-get install -y clang-3.4 llvm-3.4
RUN apt-get install -y emscripten
RUN apt-get install -y build-essential

VOLUME ["/build"]
WORKDIR /build

