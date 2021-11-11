# build environment
FROM node:15.14.0 as build

WORKDIR /app

COPY package*.json ./

RUN yarn install
COPY . ./
RUN yarn build

# production environment
FROM nginx:stable-alpine

ENV PORT=3000

ENV NGINX_PORT=$PORT

COPY nginx.default.conf.template /etc/nginx/templates/default.conf.template
COPY --from=build /app/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
