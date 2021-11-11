FROM node:lts-alpine

WORKDIR /bot

COPY . .

RUN yarn install

ENTRYPOINT ["yarn", "start"]