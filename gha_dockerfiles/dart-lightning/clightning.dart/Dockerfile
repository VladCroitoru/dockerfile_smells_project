FROM ubuntu:20.04
LABEL mantainer="Vincenzo Palazzo vincenzopalazzodev@gmail.com"

# Ubuntu utils
RUN apt-get update && apt-get install -y \
    software-properties-common wget && \
    sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -' && \
    sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list' && \
    apt-get update && apt-get install -y dart

# Install bitcoin core and lightningd (last version)
RUN add-apt-repository ppa:luke-jr/bitcoincore
RUN apt-get update  && apt-get install -y bitcoind libsodium-dev libpq-dev

ENV CLIGHTNING_VERSION=0.10.1

RUN wget https://github.com/ElementsProject/lightning/releases/download/v$CLIGHTNING_VERSION/clightning-v$CLIGHTNING_VERSION-Ubuntu-20.04.tar.xz && \
    tar -xvf clightning-v$CLIGHTNING_VERSION-Ubuntu-20.04.tar.xz -C /opt && cd /opt && \
    mv usr clightning-v$CLIGHTNING_VERSION

RUN rm -r clightning-v$CLIGHTNING_VERSION-Ubuntu-20.04.tar.xz

ENV PATH=/opt/clightning-v$CLIGHTNING_VERSION/bin:$PATH

WORKDIR workdir

CMD ["./entrypoint.sh"]