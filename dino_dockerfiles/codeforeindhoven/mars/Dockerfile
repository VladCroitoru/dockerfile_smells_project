FROM php:5-apache

RUN apt-get update && apt-get install -y libpq-dev php5-pgsql && docker-php-ext-install pgsql pdo pdo_pgsql \
  && rm -rf /var/lib/apt/lists/*


ENV DB_HOST localhost
ENV DB_NAME mars
ENV DB_USER mars
ENV DB_PASSWORD secret
ENV DB_PORT 5432

ENV MAIL_HOST localhost
ENV MAIL_USER mailuser
ENV MAIL_PASSWORD mailpassword
ENV MAIL_PORT 587
ENV MAIL_FROM test@example.com

ENV MAIL_SMTP_SECURE tls
ENV MAIL_SMTP_AUTH true

COPY . /var/www/html/

COPY dbparams.docker.php /var/www/html/mars-server/dbparams.php
COPY mailparams.docker.php /var/www/html/mars-server/mailparams.php
