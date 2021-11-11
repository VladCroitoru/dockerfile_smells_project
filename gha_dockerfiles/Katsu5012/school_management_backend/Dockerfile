FROM node:16.0

RUN npm i -g @nestjs/cli

WORKDIR /api-server
COPY package*.json /api-server/


RUN npm install
COPY . .
CMD [ "npm", "run", "start:dev"]