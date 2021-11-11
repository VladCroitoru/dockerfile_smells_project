FROM node:14-alpine

WORKDIR /app

COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN npm install

COPY . /app/
RUN npx tsc

EXPOSE 80
ENV ETHEREUM_URL http://localhost:8545/
ENV POLLING_FREQUENCY_SECONDS 5

ENTRYPOINT [ "node", "output/WebServer.js" ]
