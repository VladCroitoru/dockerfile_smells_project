FROM strapi/base:12-alpine

WORKDIR /srv/app

COPY package.json .

COPY yarn.lock .

RUN yarn

COPY . .

ENV NODE_ENV=production

RUN yarn build

CMD ["yarn", "start"]