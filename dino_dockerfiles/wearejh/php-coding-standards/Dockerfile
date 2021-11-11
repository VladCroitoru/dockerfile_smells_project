FROM php:7.1-alpine

ENV CODESNIFFER_VERSION 3.2.3

RUN curl \
        -L \
        -o /usr/local/bin/phpcs \
        "https://github.com/squizlabs/PHP_CodeSniffer/releases/download/$CODESNIFFER_VERSION/phpcs.phar" \
    && chmod +x /usr/local/bin/phpcs

RUN curl \
        -L \
        -o /usr/local/bin/phpcbf \
        "https://github.com/squizlabs/PHP_CodeSniffer/releases/download/$CODESNIFFER_VERSION/phpcbf.phar" \
    && chmod +x /usr/local/bin/phpcbf

COPY Jh /etc/coding-standard/Jh

CMD ["/usr/local/bin/phpcs", "--standard=/etc/coding-standard/Jh", "--extensions=php", "-s", "/mnt"]
