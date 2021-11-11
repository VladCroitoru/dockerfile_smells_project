# syntax=docker/dockerfile:1

FROM node:14.8.0 as builder

WORKDIR /app

COPY ["package.json", "yarn.lock", "./"]

RUN yarn

COPY . .

RUN yarn build

FROM nginx:latest

COPY --from=builder /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/docs/.vuepress/dist /usr/share/nginx/html/


