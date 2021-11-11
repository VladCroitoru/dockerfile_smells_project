FROM php:5.6-alpine

USER root

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"\
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer \
    && php -r "copy('https://phar.phpunit.de/phpunit-5.7.phar', 'phpunit-5.7.phar');" \
    && chmod +x phpunit-5.7.phar \
    && mv phpunit-5.7.phar /usr/local/bin/phpunit \
    && apk update \
    && apk add build-base \
    && apk add --update --virtual autoconf \
    && pecl install xdebug \
    && docker-php-ext-enable xdebug


##install phploc
RUN curl -OL https://phar.phpunit.de/phploc.phar \
    && chmod +x phploc.phar \
    && mv phploc.phar /usr/local/bin/phploc \
    && phploc --version

    ##install PHP CodeSniffer
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar \
    && chmod +x phpcs.phar \
    && mv phpcs.phar /usr/local/bin/phpcs \
    && phpcs --version \
    && curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar\
    && chmod +x phpcbf.phar \
    && mv phpcbf.phar /usr/local/bin/phpcbf \
    && phpcbf --version

RUN curl -OL http://static.pdepend.org/php/latest/pdepend.phar \
    && chmod +x pdepend.phar \
    && mv pdepend.phar /usr/local/bin/pdepend \
    && pdepend --version

##install phpmd
RUN curl -OL http://static.phpmd.org/php/latest/phpmd.phar \
    && chmod +x phpmd.phar \
    && mv phpmd.phar /usr/local/bin/phpmd \
    && phpmd --version

##install phpcpd
RUN curl -OL https://phar.phpunit.de/phpcpd.phar \
    && chmod +x phpcpd.phar \
    && mv phpcpd.phar /usr/local/bin/phpcpd \
    && phpcpd --version

##install phpdox
RUN apk update \
    && apk add libxslt libxslt-dev \
    && docker-php-ext-install xsl \
    && curl -OL http://phpdox.de/releases/phpdox.phar \
    && chmod +x phpdox.phar \
    && mv phpdox.phar /usr/local/bin/phpdox \
    && phpdox --version

    # && adduser -u 1000 jenkins -D
# USER jenkins
