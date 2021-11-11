FROM node:14.18.0-alpine3.11 as build-stage
WORKDIR /app
COPY package*.json ./
RUN yarn
COPY ./ .
RUN yarn build

FROM nginx:1.20.1-alpine as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /usr/share/nginx/html/frontend/
COPY nginx.conf /etc/nginx/conf.d/default.conf
