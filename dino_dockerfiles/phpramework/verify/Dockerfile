FROM quay.io/phpramework/composer:1.3.2

MAINTAINER phpramework <phpramework@gmail.com>

ENV FRAMEWORK=unknown \
    URI_JSON=/json \
    URI_DB=/db \
    URI_QUERIES=/queries/ \
    URI_UPDATES=/updates/ \
    URI_FORTUNES=/fortunes \
    URI_PLAINTEXT=/plaintext \
    CODECEPT_VERSION=2.2.9 \
    ROBO_VERSION=1.0.5

RUN curl -L http://codeception.com/releases/$CODECEPT_VERSION/codecept.phar > /usr/local/bin/codecept \
    && chmod +x /usr/local/bin/codecept \
    && curl -L https://github.com/consolidation/Robo/releases/download/$ROBO_VERSION/robo.phar > /usr/local/bin/robo \
    && chmod +x /usr/local/bin/robo \
    && composer global require flow/jsonpath

RUN rm -rf /var/cache/apk/* /var/tmp/* /tmp/* $COMPOSER_HOME/cache/*

RUN mkdir -p /result \
    && chmod -R 0777 /result
VOLUME /result

COPY tests /project/tests
COPY codeception.yml /project/codeception.yml
COPY RoboFile.php /project/RoboFile.php

ENTRYPOINT ["robo", "verify"]
