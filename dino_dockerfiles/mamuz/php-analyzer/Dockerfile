FROM php:7-alpine

RUN apk add --no-cache bash curl git graphviz alpine-sdk autoconf openjdk8-jre-base

RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \
 && echo "date.timezone=${PHP_TIMEZONE:-UTC}" > "$PHP_INI_DIR/conf.d/date_timezone.ini"

ENV PATH "/usr/bin:$PATH"

RUN curl -sSL http://xdebug.org/files/xdebug-2.5.4.tgz | tar zx
RUN cd xdebug-2.5.4 && phpize && ./configure && make -j && make install

RUN curl -sSL http://apache.mirror.digionline.de/jmeter/binaries/apache-jmeter-3.2.tgz | tar -zx \
 && ln -s /apache-jmeter-3.2/bin/jmeter /usr/bin/jmeter

COPY usr /usr

RUN curl -OsSL https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer \
 && curl -OsSL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod +x phpcs.phar && mv phpcs.phar /usr/bin/phpcs \
 && curl -OsSL https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar && chmod +x phpcbf.phar && mv phpcbf.phar /usr/bin/phpcbf \
 && curl -OsSL http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar && chmod +x php-cs-fixer-v2.phar && mv php-cs-fixer-v2.phar /usr/bin/php-cs-fixer \
 && curl -OsSL https://static.phpmd.org/php/latest/phpmd.phar && chmod +x phpmd.phar && mv phpmd.phar /usr/bin/phpmd \
 && curl -OsSL https://phar.phpunit.de/phpcpd.phar && chmod +x phpcpd.phar && mv phpcpd.phar /usr/bin/phpcpd \
 && curl -OsSL https://phar.phpunit.de/phpdcd.phar && chmod +x phpdcd.phar && mv phpdcd.phar /usr/bin/phpdcd \
 && curl -OsSL https://phar.phpunit.de/phploc.phar && chmod +x phploc.phar && mv phploc.phar /usr/bin/phploc \
 && curl -OsSL https://raw.github.com/mamuz/PhpDependencyAnalysis/master/download/phpda.pubkey && mv phpda.pubkey /usr/bin/phpda.pubkey \
 && curl -OsSL https://raw.github.com/mamuz/PhpDependencyAnalysis/master/download/phpda && chmod +x phpda && mv phpda /usr/bin/phpda \
 && curl -OsSL http://get.sensiolabs.org/security-checker.phar && chmod +x security-checker.phar && mv security-checker.phar /usr/bin/security-checker \
 && curl -OsSL https://github.com/phpmetrics/PhpMetrics/releases/download/v2.2.0/phpmetrics.phar && chmod +x phpmetrics.phar && mv phpmetrics.phar /usr/bin/phpmetrics \
 && wget https://raw.githubusercontent.com/phpmetrics/ComposerExtension/master/composer-extension.phar && chmod +x composer-extension.phar && mv composer-extension.phar /usr/bin/composer-extension

WORKDIR /app
