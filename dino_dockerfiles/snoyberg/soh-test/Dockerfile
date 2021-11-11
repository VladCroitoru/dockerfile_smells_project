FROM ubuntu:14.04

ENV HOME /app
ENV LANG en_US.UTF-8
WORKDIR ["/app"]

RUN locale-gen en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common python-software-properties
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:hvr/ghc -y
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cabal-install-1.20 ghc-7.8.4 alex-3.1.3 happy-1.19.4 sudo wget unzip zlib1g-dev

ENV PATH /app/.cabal/bin:/usr/local/sbin:/usr/local/bin:/opt/ghc/7.8.4/bin:/opt/cabal/1.20/bin:/opt/alex/3.1.3/bin:/opt/happy/1.19.4/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN cabal update
RUN wget https://www.stackage.org/lts/cabal.config
RUN cabal install classy-prelude-yesod temporary

ADD soh-test.hs /app/soh-test.hs
ADD defcode.hs /app/defcode.hs
RUN cd /app && ghc -threaded -O2 -rtsopts -with-rtsopts=-N soh-test.hs
RUN chown -R nobody /app

ADD run.sh /app/run.sh
CMD ["/app/run.sh"]
