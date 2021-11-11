FROM node:boron

RUN git clone https://github.com/EthereumEx/eth-net-intelligence-api.git /var/lib/ethStatsApi
WORKDIR /var/lib/ethStatsApi
RUN npm install

ENTRYPOINT ["npm", "start"]