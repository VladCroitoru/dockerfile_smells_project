# Service status checker
FROM php:5-apache

WORKDIR /var/www/html
EXPOSE 80

ENTRYPOINT ["bash", "entrypoint.sh"]
CMD ["file", "services.json"]

COPY . /var/www/html
