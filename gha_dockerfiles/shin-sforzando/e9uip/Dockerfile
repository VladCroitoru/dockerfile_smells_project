FROM node:16-buster

RUN apt-get update && apt-get install -y git make yarn

WORKDIR /app
RUN chmod g+w /app

COPY package*.json ./
COPY yarn.lock ./

RUN yarn install --ignore-optional

ENV PATH /app/node_modules/.bin:$PATH

COPY . .

CMD ["nuxt-ts"]
