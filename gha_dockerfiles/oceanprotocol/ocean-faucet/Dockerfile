FROM node:12

COPY package*.json /usr/src/app/
WORKDIR /usr/src/app
RUN npm install 

COPY . /usr/src/app
ENV DB_PASSWORD='pass'
ENV DB_USER='user'
ENV DB_HOST='localhost'
ENV DB_PORT='27017'
ENV DB_NAME='faucet'
ENV RPC='xxx'
ENV SEED_PHRASE='xxx'
ENV TOKEN_AMOUNT=200
ENV TOKEN_CONTRACT_ADDRESS=0x
ENV PORT=4000
ENV COOLING_PERIOD_IN_HOURS=24

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
