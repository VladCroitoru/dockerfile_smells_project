FROM ilkka/haskell-platform-stackage

MAINTAINER Ilkka Laukkanen <ilkka@fastmail.fm>

RUN cabal update && \
  cabal install alex happy yesod-bin --force-reinstalls
