FROM node:8.9-alpine as angular-built
WORKDIR /usr/src/app
RUN npm i -g @angular/cli
COPY package.json package.json
RUN npm install --silent
COPY . .
ARG target
RUN ng build --target=production --build-optimizer

FROM nginx:alpine
LABEL author="Scott Kraemer"
#COPY --from=angular-built /usr/src/app/dist /usr/share/nginx/html
COPY --from=angular-built /usr/src/app/dist /var/www/public/
COPY .docker/config/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80 443
CMD [ "nginx", "-g", "daemon off;" ]

# To build:
# From web directory
# docker build --tag whereuatv2/web .