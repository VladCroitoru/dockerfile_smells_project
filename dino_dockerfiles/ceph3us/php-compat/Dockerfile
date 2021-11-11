FROM library/php:7-cli-alpine

# install composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
  && wget -q -O /tmp/expected.sha https://composer.github.io/installer.sig \
  && php -r 'echo hash_file("SHA384", "composer-setup.php") . "\n";' > /tmp/actual.sha \
  && cmp -s /tmp/expected.sha /tmp/actual.sha \
  && php composer-setup.php --quiet \
  && rm composer-setup.php \
  && rm /tmp/*.sha

ENV PATH "$PATH:/root/.composer/vendor/bin/"

# install phpcs
RUN php composer.phar global require --prefer-stable "squizlabs/php_codesniffer=*"

# download PHPCompatibility sniff
RUN php composer.phar global require --prefer-stable "wimg/php-compatibility=*" \
  && phpcs --config-set installed_paths /root/.composer/vendor/wimg/php-compatibility

ENV PHP_CHECK_MIN "7.0"
ENV PHP_CHECK_MAX "7.2"

WORKDIR /code

ADD run-checks.sh /usr/local/bin/run-checks.sh
CMD ["/bin/sh", "/usr/local/bin/run-checks.sh"]
