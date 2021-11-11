FROM nginx:1.19.8

WORKDIR /var/www/poolc.org
COPY ./build .
COPY ./nginx.conf /etc/nginx/conf.d/poolc.org.conf

CMD ["nginx", "-g", "daemon off;"]
