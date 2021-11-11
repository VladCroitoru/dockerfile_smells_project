FROM node:alpine as build
workdir /workspace/app

COPY package.json .
COPY angular.json .
COPY tsconfig.json .
COPY src src

RUN npm install
RUN npm run-script build

FROM nginx   

ARG DIST_FOLDER=/workspace/app/dist 

## Copy our default nginx config
COPY nginx/default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

COPY --from=build ${DIST_FOLDER} /usr/share/nginx/html/

RUN chmod -R 777 /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]