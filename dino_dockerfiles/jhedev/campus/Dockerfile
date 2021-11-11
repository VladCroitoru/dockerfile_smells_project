#Heavily inspired by https://github.com/tazjin/herbert/blob/master/Dockerfile
#Thanks @tazjin
FROM haskell:7.8
MAINTAINER Joel Hermanns <joel.hermanns@gmail.com>

ENV PORT=3000
RUN cabal update && mkdir -p /opt/campus

WORKDIR /opt/campus

ADD ./campus.cabal /opt/campus/campus.cabal
RUN cabal sandbox init && \
    cabal install --only-dependencies -j

ADD . /opt/campus
RUN  cabal clean && cabal configure && cabal build

RUN cp /opt/campus/dist/build/campus/campus /usr/bin/campus && \
    cabal clean && rm -rf /opt/campus/.cabal-sandbox

ENTRYPOINT ["/usr/bin/campus"]
CMD []
