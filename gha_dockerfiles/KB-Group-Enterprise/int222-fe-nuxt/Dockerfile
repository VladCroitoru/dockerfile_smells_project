FROM node:14.16-alpine3.10 as step01
WORKDIR /frontend/src
COPY ./package.json /frontend/src/package.json
RUN npm install
COPY . /frontend/src
RUN npm run generate

FROM nginx:alpine as prod
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
WORKDIR /usr/share/nginx/html
COPY --from=step01 /frontend/src/dist .