FROM node:14-alpine as development

WORKDIR /grupogazin/monorepo

RUN npm i lerna -g

COPY package.json .
COPY packages/backend ./packages/backend
COPY packages/web ./packages/web
COPY packages/components ./packages/components

COPY package.json  lerna.json ./

RUN lerna bootstrap

RUN npm run mode:development
EXPOSE 3000
EXPOSE 4200


