FROM nginx:1.18.0-alpine as router

COPY nginx.conf /etc/nginx/templates/default.conf.template

FROM node:12.16-alpine as app

WORKDIR /opt/beabee-frontend

COPY . ./

RUN npm install

EXPOSE 8080

ENV HOST=0.0.0.0
ENV PORT=8080

ENV NODE_ICU_DATA=node_modules/full-icu

CMD [ "node", "./node_modules/.bin/nuxt", "start" ]
