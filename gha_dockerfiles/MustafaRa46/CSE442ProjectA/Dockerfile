FROM node:14

ENV HOME /CSE442ProjectA

WORKDIR /CSE442ProjectA

COPY . .

RUN npm install

EXPOSE $PORT

CMD [ "node", "server.js" ]

