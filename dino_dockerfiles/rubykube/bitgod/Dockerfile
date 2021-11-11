FROM node:9-alpine

LABEL maintainer ashanaakh@heliostech.fr

ENV BITGO_VERSION 4.18.1
ENV HOME /home/node
ENV PORT 19332

RUN apk update && apk upgrade
RUN apk add --no-cache alpine-sdk wget bitcoin bitcoin-cli python
RUN apk add --no-cache bitcoin bitcoin-cli

COPY config/bitcoin.conf ${HOME}/.bitcoin/bitcoin.conf
COPY config/bitgod.conf ${HOME}/.bitgod/bitgod.conf

RUN wget https://github.com/BitGo/bitgod/archive/${BITGO_VERSION}.tar.gz
RUN tar -xf ${BITGO_VERSION}.tar.gz

WORKDIR bitgod-${BITGO_VERSION}

RUN npm install

USER node

CMD ./bin/bitgod -conf ${HOME}/.bitgod/bitgod.conf

EXPOSE ${PORT}