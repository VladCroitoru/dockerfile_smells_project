FROM node:14-buster-slim as build-frontend

RUN apt-get update && \
    apt-get upgrade -y

COPY package.json ./
COPY yarn.lock ./

RUN apt-get install -y build-essential python

WORKDIR /app

COPY ./app/package.json .
RUN yarn install --non-interactive --network-timeout 600000

COPY ./app .
RUN yarn build


FROM node:14-buster-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove -y

RUN apt-get install -y build-essential python

COPY package.json ./
COPY yarn.lock ./

WORKDIR /api
COPY ./api/package.json .
RUN yarn install --non-interactive --network-timeout 600000

COPY ./api .
RUN yarn build

COPY --from=build-frontend /app/dist ./public
ENTRYPOINT [ "yarn", "start" ]
