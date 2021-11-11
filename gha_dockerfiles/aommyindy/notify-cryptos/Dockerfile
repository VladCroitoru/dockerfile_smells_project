FROM node:14-alpine

WORKDIR /app
COPY package*.json ./yarn.lock ./

RUN yarn
COPY . .
RUN yarn build

RUN chown -Rh node:node /app

USER node
CMD ["node", "dist/index.js"]