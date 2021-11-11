FROM node
WORKDIR /app
RUN apt-get update
RUN apt-get install -y git python openssl curl bash redis-tools jq
RUN npm install -g web3
RUN npm install -g truffle
COPY ./packages/app /node/app
RUN apt-get install -y build-essential
RUN cd /node/app && npm i --only=production && cd -
