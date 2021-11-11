# FROM node:14.13.1
FROM node:lts-alpine as build-stage
RUN npm i -g http-server

WORKDIR /app

COPY package*.json ./
RUN apk update && apk add bash

RUN npm install
RUN npm rebuild node-sass

# COPY . .

# RUN npm run build

EXPOSE 8080


# CMD [ "http-server", "dist" ]

# FROM node:lts-alpine as build-stage
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . .
# RUN npm run build

# # production stage
# # FROM nginx:stable-alpine as production-stage
# # COPY --from=build-stage /app/dist /usr/share/nginx/html
# # EXPOSE 80
# # CMD ["nginx", "-g", "daemon off;"]
# FROM nginx:alpine
# COPY dist/ /usr/share/nginx/html/
# COPY nginx.conf /etc/nginx/conf.d/
