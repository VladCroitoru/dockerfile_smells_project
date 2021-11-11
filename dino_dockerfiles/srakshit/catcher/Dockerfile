FROM node:8.10.0

WORKDIR /code

RUN npm install -g yarn knex

COPY . /code

RUN yarn install --production

EXPOSE 8080

CMD ["yarn", "start"]
