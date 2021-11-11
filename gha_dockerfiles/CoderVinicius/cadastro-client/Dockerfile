FROM node:14-slim

RUN npm i -g http-server

COPY ./package.json package.json
COPY ./package-lock.json package-lock.json

RUN npm install

COPY . .

RUN npm run build

CMD http-server ./build