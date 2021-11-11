FROM pam79/php-fpm
LABEL maintainer="Paapa Abdullah Morgan <paapaabdullahm@gmail.com>"

# Add Tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# Add PHPUnit
ENV PHPUNIT_VERSION 8.3.4
RUN apt update; apt install -y curl git openssh-server openssl bash; \
    wget https://phar.phpunit.de/phpunit-${PHPUNIT_VERSION}.phar; \
    chmod +x phpunit-${PHPUNIT_VERSION}.phar; \
    mv phpunit-${PHPUNIT_VERSION}.phar /usr/bin/phpunit;

COPY docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /src
VOLUME /src

ENTRYPOINT ["/bin/bash", "/docker-entrypoint.sh"]
CMD ["phpunit"]
