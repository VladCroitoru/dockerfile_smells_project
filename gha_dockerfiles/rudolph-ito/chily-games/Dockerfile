FROM node:16-alpine AS build-frontend

RUN mkdir -p /frontend
WORKDIR /frontend
COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn install --frozen-lockfile
COPY frontend/angular.json .
COPY frontend/src ./src
COPY shared ./src/app/shared
COPY frontend/tsconfig.app.json .
COPY frontend/tsconfig.json .
COPY tsconfig.json tsconfig.shared.json
RUN mkdir -p /frontend/dist/frontend
RUN yarn run build --configuration production

FROM node:16-alpine AS build-api

RUN mkdir -p /api
WORKDIR /api
COPY api/package.json .
COPY api/yarn.lock .
RUN yarn install --frozen-lockfile
COPY api/src ./src
COPY shared ./src/shared
COPY api/tsconfig.json .
COPY tsconfig.json tsconfig.shared.json
RUN yarn build
RUN cp -r ./src/assets ./dist/assets
RUN cp ./src/database/config.js ./dist/database/config.js
RUN cp -r ./src/database/migrations ./dist/database/migrations

FROM node:16-alpine as final

RUN mkdir -p /web
WORKDIR /web
COPY api/.sequelizerc.production .sequelizerc
COPY --from=build-api /api/node_modules ./node_modules
COPY --from=build-api /api/dist ./dist
COPY --from=build-frontend /frontend/dist/frontend ./dist/frontend/