FROM php:7.0-alpine

LABEL maintainer="Takács Ákos <rimelek@it-sziget.hu>"

WORKDIR /app

COPY examples /app/examples/
COPY index.php LICENSE README.md /app/

EXPOSE 80

CMD ["php", "-d", "phar.readonly=0", "-S", "0.0.0.0:80", "-t", "."]