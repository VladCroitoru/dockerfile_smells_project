FROM debian:wheezy
ENV DEBIAN_FRONTEND noninteractive

ENV GHC_VERSION 7.8.4
RUN apt-get update && apt-get install -y build-essential curl \
&& curl -L https://www.haskell.org/ghc/dist/$GHC_VERSION\
/ghc-$GHC_VERSION-x86_64-unknown-linux-deb7.tar.xz | tar xJ \
&& (cd ghc-$GHC_VERSION && ./configure && make install) \
&& rm -r ghc-$GHC_VERSION

ENV CABAL_VERSION 1.22.0.0
RUN apt-get update && apt-get install -y libgmp-dev libz-dev \
&& curl -L https://www.haskell.org/cabal/release\
/cabal-install-$CABAL_VERSION/cabal-install-$CABAL_VERSION.tar.gz | tar xz \
&& (cd cabal-install-$CABAL_VERSION && ./bootstrap.sh --global) \
&& rm -r cabal-install-$CABAL_VERSION

RUN cabal update && echo >>~/.cabal/config user-install: False
RUN cabal install lens
RUN cabal install hspec
RUN cabal install either
RUN cabal install cereal
