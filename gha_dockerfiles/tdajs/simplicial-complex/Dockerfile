FROM node:15
    
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm i

COPY . .

RUN npm link .
