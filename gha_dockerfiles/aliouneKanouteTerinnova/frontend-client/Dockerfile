FROM node:12-alpine as build

WORKDIR /usr/local/app

COPY ./ /usr/local/app/

RUN npm install

RUN npm run build

FROM nginx:latest

COPY --from=build /usr/local/app/dist/frontend-client /usr/share/nginx/html

RUN mkdir /etc/apache2
COPY .htpasswd /etc/apache2/

COPY nginx.conf /etc/nginx/nginx.conf 

# EXPOSE 80