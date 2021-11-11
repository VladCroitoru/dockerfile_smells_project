FROM haskell

RUN cabal update
RUN cabal install mtl
RUN cabal install network
RUN cabal install irc

ADD . /
WORKDIR /
RUN cabal configure
RUN cabal build
RUN cabal install

ENTRYPOINT /root/.cabal/bin/hirc-bot
