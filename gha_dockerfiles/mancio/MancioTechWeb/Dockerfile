FROM debian
MAINTAINER Andrea Mancini
RUN apt-get update
RUN apt-get install nginx -y
COPY ./build/ /var/www/html/
EXPOSE 80
CMD ["nginx","-g","daemon off;"]