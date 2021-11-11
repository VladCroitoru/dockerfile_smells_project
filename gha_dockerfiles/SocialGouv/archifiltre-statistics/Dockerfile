FROM node:15-alpine

WORKDIR /app

RUN chown node:node /app

COPY . .

#RUN yarn --frozen-lockfile --production
RUN yarn --frozen-lockfile --prefer-offline && yarn cache clean

RUN yarn build

USER node

ENV NODE_ENV=production

ENTRYPOINT ["yarn", "start"]
