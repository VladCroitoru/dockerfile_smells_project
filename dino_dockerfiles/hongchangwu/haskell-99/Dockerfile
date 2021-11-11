FROM haskell:latest

WORKDIR /build
COPY . /build

RUN stack build --system-ghc

ENTRYPOINT ["stack", "exec"]
