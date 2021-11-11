FROM node:14-alpine

WORKDIR /app

COPY . .

RUN yarn --production --frozen-lockfile --prefer-offline

RUN yarn cache clean

RUN yarn build

USER node

ENV NODE_ENV="production"

CMD ["yarn", "start"]
