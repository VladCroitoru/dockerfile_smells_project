FROM node:10

WORKDIR /app

COPY package*.json ./

RUN npm ci --only=production

COPY . /app

ENV SIGNING_SERVICE_PORT=6000

CMD [ "node", "index.js" ]
