FROM php:apache
RUN apt-get update -y && apt-get upgrade -y
COPY ./ /var/www/html/
RUN rm /var/www/html/Dockerfile
RUN rm /var/www/html/docker-compose.yml
