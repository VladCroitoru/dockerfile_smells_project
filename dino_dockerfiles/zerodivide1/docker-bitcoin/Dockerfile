FROM debian:jessie
MAINTAINER Sean Payne <seantpayne@gmail.com>

ENV BITCOIN_VERSION 0.11.0
ENV BITCOIN_DOWNLOAD_FILENAME bitcoin-$BITCOIN_VERSION-linux64.tar.gz

RUN apt-get update && \
    apt-get install -y wget && \
    wget https://bitcoin.org/bin/bitcoin-core-$BITCOIN_VERSION/$BITCOIN_DOWNLOAD_FILENAME && \
    wget https://bitcoin.org/bin/bitcoin-core-$BITCOIN_VERSION/SHA256SUMS.asc && \
    wget https://bitcoin.org/laanwj.asc && \
    wget https://bitcoin.org/gavinandresen.asc && \
    wget https://bitcoin.org/jgarzik-bitpay.asc && \
    wget https://bitcoin.org/gmaxwell.asc && \
    wget https://bitcoin.org/pieterwuille.asc && \
    wget https://bitcoin.org/laanwj-releases.asc && \
    gpg --import laanwj.asc && \
    gpg --import gavinandresen.asc && \
    gpg --import jgarzik-bitpay.asc && \
    gpg --import gmaxwell.asc && \
    gpg --import pieterwuille.asc && \
    gpg --import laanwj-releases.asc && \
    gpg --verify SHA256SUMS.asc && \
    grep -o "$(sha256sum $BITCOIN_DOWNLOAD_FILENAME)" SHA256SUMS.asc && \
    tar xzvf $BITCOIN_DOWNLOAD_FILENAME && \
    rm -v $BITCOIN_DOWNLOAD_FILENAME *.asc && \
    mv -v bitcoin-$BITCOIN_VERSION /bitcoin && \
    mkdir -p /bitcoin-data && \
    touch /bitcoin-data/.nodata

ADD start-bitcoind.sh /bitcoin/bin/start-bitcoind.sh

RUN chmod +x /bitcoin/bin/start-bitcoind.sh

VOLUME ["/bitcoin-data"]
WORKDIR /bitcoin/bin

ENTRYPOINT ["/bitcoin/bin/start-bitcoind.sh"]
