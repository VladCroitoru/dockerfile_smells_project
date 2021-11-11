# Base image:
FROM nginx:alpine

MAINTAINER Miral Achmed <miral.achmed@gmail.com>

RUN rm -f /etc/nginx/conf.d/*

RUN addgroup -g 1000 -S www-data \
 && adduser -u 1000 -D -S -G www-data www-data

COPY nginx.conf /etc/nginx/nginx.conf
# COPY app.conf /etc/nginx/conf.d/app.conf
 
EXPOSE 80 443
 
# Use the "exec" form of CMD so Nginx shuts down gracefully on SIGTERM (i.e. `docker stop`)
CMD [ "nginx", "-g", "daemon off;" ]

