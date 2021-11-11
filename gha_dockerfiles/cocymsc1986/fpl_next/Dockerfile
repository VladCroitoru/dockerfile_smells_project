FROM node:10-alpine

ARG BUILD_API_URL_VAR

ARG BUILD_API_KEY_VAR

ENV API_URL=$BUILD_API_URL_VAR

ENV API_KEY=$BUILD_API_KEY_VAR

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY package*.json ./

USER node

RUN npm install

COPY --chown=node:node . .

RUN npm run build

EXPOSE 3000

CMD [ "npm", "run", "start" ]