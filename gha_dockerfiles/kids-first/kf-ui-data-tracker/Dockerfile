FROM node:11 as build-deps
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY . ./

CMD yarn start
