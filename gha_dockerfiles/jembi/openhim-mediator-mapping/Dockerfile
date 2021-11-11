FROM node:erbium-alpine

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn

COPY . .

CMD ["yarn", "start"]

EXPOSE 3003
