# build stage

FROM node:lts-alpine as build-stage

ENV PUBLIC_PATH="/"
ENV VUE_APP_SERVER_URL="http://localhost:12000"

WORKDIR /app

COPY package*.json ./

RUN npm i

COPY . .

RUN npm run build

# production stage

FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d
# COPY nginx_config/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
