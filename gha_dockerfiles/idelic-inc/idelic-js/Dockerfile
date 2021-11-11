FROM node:12 AS build

ARG NODE_OPTIONS

COPY ./package.json ./
COPY ./yarn.lock ./
COPY ./lerna.json ./
COPY ./.eslintrc ./
COPY ./.prettierrc ./
COPY ./tsconfig.eslint.json ./
COPY ./packages ./packages

ENV NODE_OPTIONS ${NODE_OPTIONS}

RUN yarn install --pure-lockfile
RUN yarn bootstrap
RUN yarn lint
RUN yarn build
RUN yarn test
