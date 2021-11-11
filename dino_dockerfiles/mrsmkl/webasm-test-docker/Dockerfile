FROM ubuntu:17.04
MAINTAINER Sami Mäkelä

RUN apt-get update && \
  apt-get install -y wget ocaml opam libzarith-ocaml-dev m4 pkg-config zlib1g-dev apache2 psmisc sudo && \
  opam init -y

RUN apt-get install -y curl && \
  curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  apt-get install -y nodejs && \
  npm install -g ethereumjs-testrpc && \
  cd bin && \
  wget https://github.com/ethereum/solidity/releases/download/v0.4.18/solc-static-linux && \
  mv solc-static-linux solc && \
  chmod 744 solc

RUN wget https://dist.ipfs.io/go-ipfs/v0.4.11/go-ipfs_v0.4.11_linux-amd64.tar.gz && \
  tar xf go-ipfs_v0.4.11_linux-amd64.tar.gz && \
  cd go-ipfs && \
  ./install.sh && \
  ipfs init

RUN eval `opam config env` && \
   opam install cryptokit yojson -y

RUN wget -O getparity.sh https://get.parity.io && \
   bash getparity.sh -r stable && \
   (parity --chain dev &) && \
   sleep 10 && \
   killall parity

#RUN git clone https://github.com/TrueBitFoundation/ocaml-offchain webasm && \
#   cd webasm/interpreter && \
#   eval `opam config env` && \
#   make && \
#   ./wasm -m ../test/core/fac.wast

RUN git clone https://github.com/mrsmkl/webasm-solidity && \
  cd  webasm-solidity && \
  git submodule init && \
  git submodule update && \
  cd ocaml-offchain/interpreter && \
  eval `opam config env` && \
  make && \
  cd ../../node && \
  npm install && \
  cd .. && \
  ./compile.sh

# ENV PATH="${PATH}:/node-v6.11.3-linux-x64/bin"

RUN wget https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.7.2-1db4ecdc.tar.gz && \
  tar xf geth-linux-amd64-1.7.2-1db4ecdc.tar.gz && \
  cp geth-linux-amd64-1.7.2-1db4ecdc/geth /bin/geth

RUN cd webasm-solidity && \
  git pull && \
  chmod 755 kovan.sh dev.sh rinkeby.sh && \
  cd node && \
  cp app.html /var/www/html/index.html && \
  cp socketio.js /var/www/html/

EXPOSE 80 22448 4001

# ENTRYPOINT cd webasm-solidity && sh rinkeby.sh

