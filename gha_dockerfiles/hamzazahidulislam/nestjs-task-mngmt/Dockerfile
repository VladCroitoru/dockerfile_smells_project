FROM node:14

WORKDIR /usr/src/app

COPY ./package*.json ./

RUN npm install

COPY . .

USER node

EXPOSE 3000

CMD ["npm", "start:dev"]