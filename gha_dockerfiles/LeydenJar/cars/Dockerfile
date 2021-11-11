FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install
RUN npm install pm2 -g


COPY . .


EXPOSE ${APP_PORT}
CMD [ "npm", "run", "start" ]