FROM ubuntu

RUN apt-get -q update
RUN apt-get -yq install automake autoconf pkg-config libtool software-properties-common git wget

RUN git clone https://github.com/vstakhov/libucl /libucl && \
    cd /libucl && \
    ./autogen.sh && \
    ./configure --disable-debug --disable-dependency-tracking --disable-silent-rules --prefix=/usr/local/ && \
    make install && \
    rm -rf /libucl

RUN mkdir /phc-winner-argon2 && \
    wget -qO- https://github.com/P-H-C/phc-winner-argon2/archive/20161029.tar.gz | tar zx --strip-components 1 -C /phc-winner-argon2 && \
    cd phc-winner-argon2 && \
    make && make install PREFIX=/usr/local && \
    rm -rf /phc-winner-argon2

RUN add-apt-repository ppa:longsleep/golang-backports && apt-get -q update && apt-get install -yq golang-go libzmq3-dev
RUN echo "github.com/golang/snappy github.com/cihub/seelog" | xargs go get
RUN go get github.com/bitmark-inc/bitmark-cli
RUN go get github.com/bitmark-inc/bitmarkd || go install github.com/bitmark-inc/bitmarkd/command/...

