#Heavily inspired by https://github.com/tazjin/herbert/blob/master/Dockerfile
#Thanks @tazjin
FROM haskell:7.8
MAINTAINER Joel Hermanns <joel.hermanns@gmail.com>

ENV PORT=3000
RUN cabal update && mkdir -p /opt/sloppy-test

WORKDIR /opt/sloppy-test

ADD ./sloppy-test.cabal /opt/sloppy-test/sloppy-test.cabal
RUN cabal sandbox init && \
    cabal install --only-dependencies -j

ADD . /opt/sloppy-test
RUN  cabal clean && cabal configure && cabal build

RUN cp /opt/sloppy-test/dist/build/sloppy-test/sloppy-test /usr/bin/sloppy-test && \
    cabal clean && rm -rf /opt/sloppy-test/.cabal-sandbox

ENTRYPOINT ["/usr/bin/sloppy-test"]
CMD []
