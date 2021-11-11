FROM haskell:8.8.4

RUN mkdir /tmp/project

WORKDIR /tmp/project

RUN cabal update

COPY . .

RUN cabal v1-install --global

RUN rm -rf /tmp/project
