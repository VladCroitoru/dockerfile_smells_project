FROM codeception/codeception:3.1.0

WORKDIR /repo
RUN composer require -o --prefer-dist -n --no-progress ericmartel/codeception-email-mailhog flow/jsonpath
RUN docker-php-ext-install pdo_mysql
WORKDIR /project

