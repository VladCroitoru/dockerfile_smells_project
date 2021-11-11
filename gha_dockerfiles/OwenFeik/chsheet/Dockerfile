FROM node:14

WORKDIR /usr/src/chsheet_server

COPY . .

EXPOSE 8080

RUN npm install
CMD [ "node", "server/server.js" ]
