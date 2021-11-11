FROM php:7-cli-alpine

RUN curl -L https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar > /usr/local/bin/phpcs && \
    curl -L https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar > /usr/local/bin/phpcbf && \
    chmod +x /usr/local/bin/phpcs /usr/local/bin/phpcbf
