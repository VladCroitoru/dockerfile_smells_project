FROM php:7.0
RUN apt-get update \
  && apt-get install git ruby-dev ruby ruby2.1-dev cmake -y
RUN curl -L https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar -o /usr/local/bin/phpcs \
  && chmod +x /usr/local/bin/phpcs
RUN gem install pronto -v 0.8.0 && gem install pronto-phpcs
