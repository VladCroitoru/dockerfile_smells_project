FROM php:7.1-apache

COPY src/ /var/www/html/
COPY docker/ /

RUN chmod +x /build_image.sh && sleep 2 && /build_image.sh && rm /build_image.sh
