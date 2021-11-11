FROM node:slim

WORKDIR /app

COPY package.json ./
RUN npm install

COPY . ./

ENV NODE_ENV=production
ENV secure=true
ENV port=3000
ENV hostname=localhost
ENV accessToken=accessToken
ENV clientId=clientId
ENV clientSecret=clientSecret

EXPOSE 3000

ENTRYPOINT node index.js --secure=$secure --port=$port --hostname=$hostname --clientId=$clientId --clientSecret=$clientSecret --accessToken=$accessToken
