FROM node:14.14.0-alpine as build_stage

RUN mkdir -p /home/node/app
WORKDIR /home/node/app
COPY reactapp .
COPY reactapp/package.json .
COPY reactapp/.env.production .env
RUN yarn 
RUN yarn build

FROM nginx:1.16.0-alpine

COPY --from=build_stage /home/node/app/build /usr/share/nginx/html
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]