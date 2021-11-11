# 0. build stage
FROM node:alpine as build-stage
WORKDIR /app
COPY package.json yarn.lock /app/
RUN yarn
COPY ./ /app/
RUN yarn build

FROM nginx:alpine
COPY --from=build-stage /app/build/ /usr/share/nginx/html
COPY --from=build-stage /app/server/nginx.conf /etc/nginx/conf.d/default.conf
