FROM debian:jessie
RUN apt-get update && apt-get install -y haskell-platform libgc-dev llvm-dev libghc-terminfo-dev pkg-config
RUN cabal update && cabal install idris-0.9.19
RUN bash -c "ln -s /root/.cabal/bin/idris /usr/local/bin/"
WORKDIR /source
