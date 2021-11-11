# This Dockerfile builds an image with Herbert server as the entrypoint
FROM haskell:7.8
MAINTAINER Vincent Ambo <tazjin@gmail.com>

RUN apt-get update && apt-get install -y libssl-dev && cabal update && \
    mkdir -p /opt/herbert

WORKDIR /opt/herbert

# This is run here to allow Docker to cache the dependencies.
ADD ./herbert.cabal /opt/herbert/herbert.cabal
RUN cabal sandbox init && \
    cabal install --only-dependencies -j

ADD . /opt/herbert
RUN  cabal clean && cabal configure && cabal build

# Move herbert executable into place and clean up after us for a smaller image
RUN cp /opt/herbert/dist/build/herbert-bin/herbert-bin /usr/bin/herbert && \
    cabal clean && rm -rf /opt/herbert/.cabal-sandbox

VOLUME ["/etc/herbert.d", "/var/log/herbert"]
EXPOSE 1212
ENTRYPOINT ["/usr/bin/herbert"]
CMD []
