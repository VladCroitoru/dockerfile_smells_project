FROM alpine:3.7
MAINTAINER Alex Brandt <alunduil@alunduil.com>

RUN apk add --no-cache musl-dev zlib-dev
RUN apk add --no-cache cabal ghc

RUN cabal update

WORKDIR /usr/local/src/cabal-parser

COPY ./cabal-parser.cabal /usr/local/src/cabal-parser/cabal-parser.cabal
RUN cabal install -j --only-dependencies

COPY . /usr/local/src/cabal-parser
RUN cabal build -j --ghc-options="-static -optc-static -optl-static -optl-pthread"

FROM alpine:3.7
MAINTAINER Alex Brandt <alunduil@alunduil.com>

RUN apk add --no-cache ca-certificates

COPY --from=0 /usr/local/src/cabal-parser/dist/build/cabal-parser/cabal-parser /

ENTRYPOINT [ "/cabal-parser" ]
CMD [ "Heroku Compatability" ]
