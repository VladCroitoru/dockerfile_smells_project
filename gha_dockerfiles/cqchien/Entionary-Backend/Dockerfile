FROM node:alpine

ENV NODE_ENV=production

WORKDIR /src

COPY ["package.json", "yarn.lock*", "./"]

RUN yarn install --production

COPY . .

CMD [ "yarn", "start:prod" ]