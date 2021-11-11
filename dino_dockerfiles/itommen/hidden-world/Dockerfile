FROM node:9-alpine AS base
FROM base AS dependencies

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package*.json ./

FROM dependencies as build

RUN npm install

COPY . .

RUN npm run build

FROM base AS producation

WORKDIR /usr/dist/app

COPY --from=dependencies /usr/src/app/ /usr/dist/app
COPY --from=build /usr/src/app/dist/ /usr/dist/app

RUN npm install --prodcation

CMD ["node", "server/app.js"]