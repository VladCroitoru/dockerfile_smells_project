FROM richarvey/nginx-php-fpm
COPY src/ /var/www/html/
RUN rm /etc/nginx/sites-enabled/default.conf
COPY nginx-conf/ /etc/nginx/sites-enabled/
EXPOSE 80
