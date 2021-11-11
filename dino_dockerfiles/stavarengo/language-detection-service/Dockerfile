FROM stavarengo/cld2-php-language-detection-library:v0.0.4

COPY Docker/language-detection-service.conf /etc/apache2/sites-available/

COPY ./ /var/www/html/language-detection-service

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install zip unzip composer -y && \
    # Install Composer dependencies
    cd /var/www/html/language-detection-service && \
    composer install --no-dev && \
    # Enabling our Apache Site and some required Apache Modules
    rm -rf /etc/apache2/sites-enabled/* && \
    a2ensite language-detection-service.conf && \
    a2enmod rewrite && \
    service apache2 restart

WORKDIR /var/www/html/language-detection-service

EXPOSE 80

CMD ["apache2ctl", "-D", "FOREGROUND"]
