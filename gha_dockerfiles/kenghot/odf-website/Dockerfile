FROM node:dubnium
MAINTAINER thelonewolf
EXPOSE 80
RUN apt-get update && apt-get install -y nginx
RUN mkdir /odf-web
WORKDIR /odf-web
COPY . .
RUN npm install && npm run build:dev
RUN rm /etc/nginx/sites-enabled/* && cp nginx /etc/nginx/sites-enabled/ \
  && cp -r build/* /var/www/html/ && rm -rf *
CMD ["nginx", "-g", "daemon off;"]
