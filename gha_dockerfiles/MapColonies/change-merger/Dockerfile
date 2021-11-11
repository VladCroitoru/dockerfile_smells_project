FROM node:12 as build


WORKDIR /tmp/buildApp

COPY ./package*.json ./

RUN npm install
COPY . .
RUN npm run build

FROM node:12.20.1-alpine3.9 as production

RUN apk add dumb-init

ENV NODE_ENV=production
ENV SERVER_PORT=8080


WORKDIR /usr/src/app

COPY --chown=node:node package*.json ./

RUN npm ci --only=production

COPY --chown=node:node --from=build /tmp/buildApp/dist .
COPY --chown=node:node ./config ./config


USER node
EXPOSE 8080
CMD ["dumb-init", "node", "--max_old_space_size=512", "./index.js"]
