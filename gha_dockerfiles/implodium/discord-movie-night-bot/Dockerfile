FROM node:16.7.0-alpine3.14

WORKDIR /app

COPY package*.json ./

RUN npm i --only=dev

COPY . ./

RUN npm run webpack:build:prod \
    && rm -rf node_modules \
    && npm i --only=prod \
    && cp -rf node_modules dist/node_modules \
    && mkdir dist/config \
    && cp -rf config/app dist/config/app

FROM node:16.7.0-alpine3.14

ENTRYPOINT ["node", "main.js"]

WORKDIR /app

COPY --from=0 /app/dist .
