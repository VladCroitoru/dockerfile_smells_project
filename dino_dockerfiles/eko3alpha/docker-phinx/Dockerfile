FROM composer/composer
MAINTAINER Angel Alvarado <eko3alpha>

RUN composer global require 'robmorgan/phinx'
RUN docker-php-ext-install pdo pdo_mysql

ENTRYPOINT ["phinx"]
CMD ["--help"]
