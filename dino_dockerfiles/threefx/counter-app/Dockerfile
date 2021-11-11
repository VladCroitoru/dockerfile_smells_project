FROM haskell

WORKDIR /app

RUN cabal update && cabal install hedis snap

RUN cabal update && cabal install iso8601-time

EXPOSE 5000

COPY src src

RUN ghc -O2 src/Main.hs

CMD ["src/Main"]
