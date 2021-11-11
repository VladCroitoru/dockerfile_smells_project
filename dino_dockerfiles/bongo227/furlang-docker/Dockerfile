FROM ubuntu:yakkety

RUN apt-get update -q
RUN apt-get install wget -y

# Install llvm 3.9
RUN echo "deb http://apt.llvm.org/yakkety/ llvm-toolchain-yakkety-3.9 main" >> /etc/apt/sources.list
RUN echo "deb-src http://apt.llvm.org/yakkety/ llvm-toolchain-yakkety-3.9 main" >> /etc/apt/sources.list
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -
RUN apt-get install clang-3.9 clang-3.9-doc libclang-common-3.9-dev libclang-3.9-dev libclang1-3.9 libclang1-3.9-dbg libllvm-3.9-ocaml-dev libllvm3.9 libllvm3.9-dbg lldb-3.9 llvm-3.9 llvm-3.9-dev llvm-3.9-doc llvm-3.9-examples llvm-3.9-runtime clang-format-3.9 python-clang-3.9 -y

# Install golang 1.7.3
RUN wget https://storage.googleapis.com/golang/go1.7.3.linux-amd64.tar.gz
RUN tar -xf go1.7.3.linux-amd64.tar.gz
RUN mv go /usr/local
RUN rm go1.7.3.linux-amd64.tar.gz
ENV GOROOT /usr/local/go
ENV GOPATH /go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

# Install bats
RUN apt-get install git -y
RUN git clone https://github.com/sstephenson/bats.git
RUN ./bats/install.sh /usr/local
RUN rm -rf bats
