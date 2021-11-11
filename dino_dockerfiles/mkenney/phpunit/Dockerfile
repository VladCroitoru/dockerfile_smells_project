FROM mkenney/php-base:latest

MAINTAINER Michael Kenney <mkenney@webbedlam.com>

##############################################################################
# phpunit
##############################################################################

ENV PHPUNIT_VERSION 6.5.3
RUN mkdir -p /root/src \
    && cd /root/src \
    && wget https://phar.phpunit.de/phpunit-${PHPUNIT_VERSION}.phar \
    && chmod +x phpunit-${PHPUNIT_VERSION}.phar \
    && mv phpunit-${PHPUNIT_VERSION}.phar /usr/local/bin/phpunit \
    && rm -rf /root/src \
    && phpunit --version

RUN curl -o /run-as-user https://raw.githubusercontent.com/mkenney/docker-scripts/master/container/run-as-user \
    && chmod 0755 /run-as-user

ENTRYPOINT ["/run-as-user","/usr/local/bin/phpunit","--colors=always"]
