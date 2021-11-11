FROM node:14.15.4-alpine3.12 as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm build

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
