FROM node:12-alpine

EXPOSE 80

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY .babelrc /usr/src/app/
COPY src/config.js /usr/src/app/
COPY src/data_access /usr/src/app/data_access/
COPY src/database.js /usr/src/app/
COPY src/index.js /usr/src/app/
COPY package.json /usr/src/app/
COPY src/resolvers /usr/src/app/resolvers/
COPY src/server.js /usr/src/app/
COPY src/type_defs /usr/src/app/type_defs/

RUN npm install

CMD [ "./node_modules/.bin/babel-node", "index.js"]
