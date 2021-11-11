FROM node:alpine AS build

LABEL name="build"

WORKDIR /usr/app

COPY package*.json ./
RUN yarn install

COPY . .

RUN yarn build

FROM node:alpine

LABEL name="production"

WORKDIR /usr/app

COPY package*.json ./

RUN yarn install --no-lockfile --prod && yarn cache clean --all

COPY --from=build /usr/app/dist ./dist
COPY --from=build /usr/app/ormconfig.js .
COPY --from=build /usr/app/config.json .
COPY --from=build /usr/app/data.json .
COPY --from=build /usr/app/reaction.json .

ENTRYPOINT [ "yarn", "start" ]