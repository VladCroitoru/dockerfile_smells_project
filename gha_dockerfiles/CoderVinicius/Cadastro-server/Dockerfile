FROM node:14-slim

COPY ./package.json package.json
COPY ./package-lock.json package-lock.json

RUN npm install

COPY . .

CMD npm run start