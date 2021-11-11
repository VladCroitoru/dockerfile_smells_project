# build stage
FROM node:15.8.0-alpine3.13 as build-stage

WORKDIR /app

COPY . .

RUN yarn install

RUN yarn build

# production stage
FROM node:15.8.0-alpine3.13 as production-stage

WORKDIR /app

RUN yarn global add pm2

RUN chown -R node:node /app

USER node

RUN mkdir dist

COPY --chown=node:node ./package.json ./yarn.lock ./ecosystem.config.js ./

COPY --chown=node:node --from=build-stage /app/dist /app/dist

RUN yarn install --production --silent

CMD [ "pm2-runtime", "start", "ecosystem.config.js" ]
