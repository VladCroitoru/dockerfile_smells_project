FROM node:14-alpine

WORKDIR /app

COPY package.json .
COPY yarn.lock .

RUN yarn --frozen-lockfile

COPY .next/ /app/.next/
COPY public/ /app/public/
COPY next.config.js /app/
COPY knexfile.js /app/
COPY src/knex /app/src/knex/

USER node

CMD ["yarn", "start"]