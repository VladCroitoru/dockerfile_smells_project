FROM php:7-apache
RUN a2enmod rewrite
COPY . /var/www/html
ENTRYPOINT ["/var/www/html/entrypoint.sh"]
CMD ["apache2-foreground"]
