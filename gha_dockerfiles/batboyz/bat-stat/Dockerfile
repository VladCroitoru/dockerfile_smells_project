FROM node:16

COPY . /app

WORKDIR /app

RUN yarn install && yarn build

EXPOSE 3000

CMD ["node", "server.js"]