# Base image: https://hub.docker.com/_/golang/
FROM golang:1.9

ENV GOPATH /go
ENV PATH ${GOPATH}/bin:$PATH

# Install dep
RUN mkdir -p $GOPATH/src/golang.org/x \
    && git clone https://github.com/golang/time.git $GOPATH/src/golang.org/x/time
RUN git clone https://github.com/golang/sys.git $GOPATH/src/golang.org/x/sys
RUN git clone https://github.com/golang/vgo.git $GOPATH/src/golang.org/x/vgo
RUN git clone https://github.com/golang/text.git $GOPATH/src/golang.org/x/text
RUN git clone https://github.com/golang/net.git $GOPATH/src/golang.org/x/net
RUN git clone https://github.com/golang/exp.git $GOPATH/src/golang.org/x/exp
RUN git clone https://github.com/golang/perf.git $GOPATH/src/golang.org/x/perf
RUN git clone https://github.com/golang/image.git $GOPATH/src/golang.org/x/image
RUN git clone https://github.com/golang/sync.git $GOPATH/src/golang.org/x/sync
RUN git clone https://github.com/golang/tools.git $GOPATH/src/golang.org/x/tools
RUN git clone https://github.com/golang/crypto.git $GOPATH/src/golang.org/x/crypto

RUN go get -u gopkg.in/alecthomas/gometalinter.v2 \
    && gometalinter.v2 -i \
    && go get -u github.com/mitchellh/gox

# Add apt key for LLVM repository
RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -

# Add LLVM apt repository
RUN echo "deb http://apt.llvm.org/stretch/ llvm-toolchain-stretch-5.0 main" | tee -a /etc/apt/sources.list

# Install clang from LLVM repository
RUN apt-get update && apt-get install -y --no-install-recommends clang-5.0

# Set Clang as default CC
ENV set_clang /etc/profile.d/set-clang-cc.sh
RUN echo "export CC=clang-5.0" | tee -a ${set_clang} && chmod a+x ${set_clang}

# Remove cache
RUN apt-get autoremove \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*