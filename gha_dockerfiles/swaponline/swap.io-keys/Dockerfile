# build stage
ARG NODE_VERSION=14.7.0

FROM node:${NODE_VERSION} AS build-stage

RUN mkdir -p /app
WORKDIR /app

COPY package*.json ./
RUN npm install
RUN npm rebuild node-sass

COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80

