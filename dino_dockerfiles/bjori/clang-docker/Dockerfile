# Multiple versions of clang.
# Inspired by https://hub.docker.com/_/gcc/
FROM buildpack-deps:jessie

RUN echo 'deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie main' >> /etc/apt/sources.list
RUN echo 'deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie-3.8 main' >> /etc/apt/sources.list
RUN echo 'deb http://apt.llvm.org/jessie/ llvm-toolchain-jessie-3.9 main' >> /etc/apt/sources.list
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN apt-get update
RUN apt-get install -y clang-3.4 clang-3.5 clang-3.6 clang-3.7 clang-3.8 clang-3.9 clang-4.0


