
FROM kusumoto/docker-php-dev-env:php5.6

COPY . /var/www/html

WORKDIR /var/www/html

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod 777 /entrypoint.sh

RUN mkdir /ci_session

RUN chmod 777 /ci_session

RUN a2enmod rewrite

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

CMD ["apache2-foreground"]