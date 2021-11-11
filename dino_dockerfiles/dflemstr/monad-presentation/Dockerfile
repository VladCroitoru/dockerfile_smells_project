FROM zsol/haskell-platform-2013.2.0.0
RUN cabal update
RUN sudo apt-get update && sudo apt-get install -y llvm
ADD deps/vector-0.10.9.1.tar.gz /home/haskell/deps
RUN cd deps/vector-0.10.9.1 && cabal install
ADD deps/hint-0.3.3.7.tar.gz /home/haskell/deps
RUN cd deps/hint-0.3.3.7 && cabal install
ADD cloudeval.cabal /home/haskell/cloudeval.cabal
ADD LICENSE /home/haskell/LICENSE
RUN cabal install --only-dependencies
ADD src /home/haskell/src
RUN cabal configure && cabal build
ADD deps/MonadRandom-0.1.12.tar.gz /home/haskell/deps
RUN cd deps/MonadRandom-0.1.12 && cabal install
ADD static /home/haskell/static

ENTRYPOINT ["/home/haskell/dist/build/cloudeval/cloudeval", "/home/haskell/static"]
EXPOSE 3000
MAINTAINER David Flemström <david.flemstrom@gmail.com>
