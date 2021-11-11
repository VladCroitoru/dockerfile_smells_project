FROM ubuntu:14.04

ENV VERSION 0.14
ENV FULL_VERSION ${VERSION}.2
ENV BITCOIN_UASF_VERSION bitcoin-${FULL_VERSION}-bip148_segwit0.3
ENV BITCOIN_DIR /bitcoin-${FULL_VERSION}

RUN apt-get update && \
    apt-get install -qy wget uuid-runtime

RUN useradd uasf -m -d /home/uasf -s /bin/bash
RUN wget https://uasf.bitcoinreminder.com/core-${FULL_VERSION}-uasfsegwit0.3/${BITCOIN_UASF_VERSION}-x86_64-linux-gnu.tar.gz
RUN tar xf ${BITCOIN_UASF_VERSION}-x86_64-linux-gnu.tar.gz

# Verify signed binary
RUN wget https://raw.githubusercontent.com/UASF/gitian.sigs/master/${FULL_VERSION}-uasfsegwit0.3-linux/laanwj/bitcoin-linux-${VERSION}-build.assert
RUN wget https://github.com/UASF/gitian.sigs/raw/master/${FULL_VERSION}-uasfsegwit0.3-linux/laanwj/bitcoin-linux-${VERSION}-build.assert.sig

# Checking if sha256 is correct
RUN grep $(sha256sum ${BITCOIN_UASF_VERSION}-x86_64-linux-gnu.tar.gz) bitcoin-linux-${VERSION}-build.assert

# Checking if binary was actually signed by Wladimir J. van der Laan
RUN gpg --keyserver pgp.mit.edu --recv-keys 2346C9A6
# gpg: key 2346C9A6: public key "Wladimir J. van der Laan <laanwj@gmail.com>" imported
# gpg: key 2346C9A6: public key "Wladimir J. van der Laan <laanwj@visucore.com>" imported
RUN gpg --verify ./bitcoin-linux-${VERSION}-build.assert.sig


# Notice: Mount volume if you want to preserve .bitcoin data
ADD bitcoin.conf /home/uasf/.bitcoin/bitcoin.conf
RUN mkdir -p /home/uasf/.bitcoin/blocks
RUN chown uasf /home/uasf/.bitcoin -Rc

USER uasf
WORKDIR /home/uasf

ADD run.sh /run.sh

VOLUME ['/home/uasf/.bitcoin/blocks']
EXPOSE 8333
CMD bash /run.sh