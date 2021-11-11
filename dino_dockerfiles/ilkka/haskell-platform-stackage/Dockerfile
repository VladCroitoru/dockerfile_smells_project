FROM ubuntu:14.04

ENV HOME /root
ENV PATH /root/.cabal/bin:$PATH
ENV HASKELL_PLATFORM_VERSION 2014.2.0.0

RUN apt-get update && \
  apt-get install -y zlib1g-dev curl libgmp10 && \
  cd /usr/lib/x86_64-linux-gnu && \
  ln -s libgmp.so.10 libgmp.so && \
  cd / && \
  curl -O http://www.haskell.org/platform/download/2014.2.0.0/haskell-platform-${HASKELL_PLATFORM_VERSION}-unknown-linux-x86_64.tar.gz && \
  tar xzf haskell-platform-${HASKELL_PLATFORM_VERSION}-unknown-linux-x86_64.tar.gz && \
  rm -f haskell-platform-${HASKELL_PLATFORM_VERSION}-unknown-linux-x86_64.tar.gz && \
  /usr/local/haskell/ghc-7.8.3-x86_64/bin/activate-hs && \
  cabal update && \
  sed -i "s%^remote-repo: .*%remote-repo: stackage:http://www.stackage.org/stackage/46bb2d7487546939e22612e7d757f1df5a5163e9%" /root/.cabal/config && \
  cabal update

WORKDIR /root
CMD ["bash"]

