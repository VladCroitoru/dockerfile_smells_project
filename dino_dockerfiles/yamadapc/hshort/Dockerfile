FROM fpco/stack-build:latest

RUN stack update

ADD ./hshort.cabal /app/hshort.cabal
WORKDIR /app

ADD . /app/
RUN stack build
