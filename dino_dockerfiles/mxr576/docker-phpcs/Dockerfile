FROM composer:latest

USER root

RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> $HOME/.bashrc
RUN composer global config bin-dir /usr/local/bin && \
    composer global config vendor-dir /var/lib/composer/vendor && \
	composer global config minimum-stability dev && \
    composer global config prefer-stable true && \
    composer global config optimize-autoloader true && \
    composer global config preferred-install dist && \
    composer global config sort-packages true

RUN composer global require --no-suggest hirak/prestissimo
RUN composer global require --no-suggest dealerdirect/phpcodesniffer-composer-installer \
    drupal/coder \
    wimg/php-compatibility

USER www-data

VOLUME /data

WORKDIR /data

ENTRYPOINT ["phpcs"]
CMD ["-i"]
