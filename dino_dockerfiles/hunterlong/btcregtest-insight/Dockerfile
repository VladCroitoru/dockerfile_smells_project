FROM node:9.11.1

RUN node -v
RUN npm -v

RUN mkdir -p /data
RUN mkdir -p /data/bitcoin

RUN apt update
RUN apt-get install -y libzmq3-dev build-essential screen
RUN npm install -g node-gyp

RUN npm install -g --unsafe-perm=true bitcore@latest

RUN bitcore create /data/bitcore —-regtest
ADD bitcore-node.json /data/bitcore/

EXPOSE 3001
EXPOSE 8333

WORKDIR /data/bitcore
RUN bitcore install insight-api insight-ui

RUN cp ./node_modules/bitcore-node/bin/bitcoin-0.12.1/bin/bitcoin-cli /usr/local/bin/
RUN cp ./node_modules/bitcore-node/bin/bitcoin-0.12.1/bin/bitcoind /usr/local/bin/

RUN mkdir /root/.bitcoin
ADD bitcoin.conf /data/bitcoin/
ADD wallet.backup /data/bitcoin/
ADD startup.sh /data/bitcore/
ADD bitcoin.conf /root/.bitcoin/

ENTRYPOINT ./startup.sh