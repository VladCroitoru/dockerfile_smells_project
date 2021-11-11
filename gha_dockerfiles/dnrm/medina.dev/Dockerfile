FROM node:14
WORKDIR /app

COPY ./package.json .
COPY ./yarn.lock .

RUN yarn install
COPY . .

EXPOSE 3000

RUN yarn build

CMD ["yarn", "start"]