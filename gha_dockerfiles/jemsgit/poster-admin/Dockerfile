FROM node:14

WORKDIR /usr/src/app

COPY package.json ./
COPY config.js ./

RUN npm install

ADD dist dist
ADD src/server src/server

EXPOSE 3000

CMD [ "node", "src/server/server.js" ]
