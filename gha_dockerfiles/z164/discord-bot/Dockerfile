FROM node:16

WORKDIR /discord-bot

COPY package*.json ./

RUN npm i

COPY . .

RUN npm run build

CMD [ "npm", "run", "start:prod" ]