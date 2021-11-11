FROM node:10.9.0-alpine AS build-env
WORKDIR /app
ADD . /app
RUN cd /app && npm i && npm run build
FROM nginx:alpine
ADD nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-env /app/dist /var/www/html
EXPOSE  80
