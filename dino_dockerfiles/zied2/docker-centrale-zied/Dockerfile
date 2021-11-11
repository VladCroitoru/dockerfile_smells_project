FROM ubuntu:16.04 

RUN apt-get update && apt-get -y install nginx

ADD index.html /var/www/html/index.html

VOLUME /var/www/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
