FROM node:16.8.0-buster

WORKDIR /usr/src/app

COPY package.json ./

RUN npm install

COPY . .

EXPOSE 4000

CMD npm run start:admin
