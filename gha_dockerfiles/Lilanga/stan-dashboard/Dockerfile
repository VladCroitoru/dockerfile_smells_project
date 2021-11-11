# build image
FROM node:12.16.1-buster AS build

WORKDIR /app
COPY package.json .
RUN yarn

COPY ./src ./src 
COPY .babelrc .
RUN yarn build

COPY ./server ./server
RUN yarn build-server

#runtime image
FROM node:12.16.1-alpine3.11

WORKDIR /app

COPY --from=build /app/dist/ ./dist/ 
COPY --from=build /app/node_modules ./node_modules

CMD ["node", "./dist"]