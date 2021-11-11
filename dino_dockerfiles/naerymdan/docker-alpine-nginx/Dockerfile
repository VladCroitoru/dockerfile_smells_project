FROM alpine:edge
MAINTAINER Naerymdan <vincent.dev@gmail.com>
##
# Nginx: 1.9.X
##

# Nginx 1.9
RUN apk add --update nginx && \
    rm -rf /var/cache/apk/* && \
    chown -R nginx:www-data /var/lib/nginx

COPY nginx.conf  /etc/nginx/nginx.conf

#Volume for website files
VOLUME /usr/share/nginx/html

#Set port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]