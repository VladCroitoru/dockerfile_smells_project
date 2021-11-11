FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run compile

EXPOSE 3000

CMD [ "npm", "run", "start" ]