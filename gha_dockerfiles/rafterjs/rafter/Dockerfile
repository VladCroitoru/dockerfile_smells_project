FROM node:latest

RUN mkdir /app
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json yarn.lock .eslintignore .eslintrc.js .prettierrc.js lerna.json ./
RUN yarn install

COPY packages/ app/packages/
RUN yarn bootstrap