FROM node:14-alpine

WORKDIR /usr/src/app

RUN yarn global add pnpm

COPY . .

RUN pnpm i

RUN pnpm m run build