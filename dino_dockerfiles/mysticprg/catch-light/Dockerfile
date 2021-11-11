FROM node:8.1.0
MAINTAINER mysticPrg <mysticPrg@gmail.com>

EXPOSE 80
EXPOSE 8080
EXPOSE 3000

ADD ./ /app
WORKDIR /app

RUN npm install -g yarn
RUN yarn install

CMD npm start
