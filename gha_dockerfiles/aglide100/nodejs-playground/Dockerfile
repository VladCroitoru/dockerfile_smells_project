FROM node:lts-alpine

WORKDIR /usr/src/app

COPY package*.json ./

COPY . . 

RUN npm install --no-optional

RUN npm run build

EXPOSE 5000

CMD "npm" "run" "start"