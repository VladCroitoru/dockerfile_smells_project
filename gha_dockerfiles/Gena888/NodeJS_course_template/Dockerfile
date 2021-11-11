FROM node:14-alpine3.14

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE $PORT

CMD [ "node", "--experimental-modules", "--es-module-specifier-resolution=node", "dist/server.js"]