FROM node:9.11.1

RUN node -v
RUN npm -v

RUN mkdir -p /data
RUN mkdir -p /data/bitcoin

RUN apt update
RUN apt-get install -y libzmq3-dev build-essential screen
RUN npm install -g node-gyp

RUN npm install -g --unsafe-perm=true litecore-node@latest

RUN litecore-node create /data/bitcore —-regtest
ADD litecore-node.json /data/bitcore/

EXPOSE 3005
EXPOSE 8333

WORKDIR /data/bitcore
RUN litecore-node install insight-lite-api insight-lite-ui

RUN cp ./node_modules/litecore-node/bin/litecoin-0.13.2/bin/litecoin-cli /usr/local/bin/
RUN cp ./node_modules/litecore-node/bin/litecoin-0.13.2/bin/litecoind /usr/local/bin/

RUN mkdir /root/.litecoin
ADD litecoin.conf /data/bitcoin/bitcoin.conf
ADD wallet.backup /data/bitcoin/
ADD startup.sh /data/bitcore/
ADD litecoin.conf /root/.litecoin/

ENTRYPOINT ./startup.sh