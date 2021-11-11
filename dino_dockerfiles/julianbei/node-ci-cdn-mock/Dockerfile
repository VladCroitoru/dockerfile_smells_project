FROM mhart/alpine-node:6

RUN mkdir /server
WORKDIR /server

RUN npm install --global yarn

COPY ./package.json ./package.json
RUN yarn install --production

COPY ./server.js ./server.js

RUN mkdir ./app
WORKDIR /server/app

CMD ["node", "/server/server.js"]
