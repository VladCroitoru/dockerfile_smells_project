FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

ENV PORT=3028

EXPOSE 3028

CMD [ "node", "index.js" ]
