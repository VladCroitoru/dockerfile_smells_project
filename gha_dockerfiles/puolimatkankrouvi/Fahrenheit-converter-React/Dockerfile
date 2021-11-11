FROM node:14-alpine as build

WORKDIR /usr/src/app

COPY package.json ./
COPY yarn.lock ./
RUN yarn install --silent

COPY . .

RUN yarn run build

FROM nginx

COPY --from=build  /usr/src/app/build /usr/share/nginx/html