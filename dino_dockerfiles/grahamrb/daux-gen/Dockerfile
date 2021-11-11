FROM composer/composer:1.1-alpine
MAINTAINER Graham Rivers-Brown <graham@extg.net>

VOLUME ["/var/docs", "/var/static"]
RUN composer global require justinwalsh/daux.io

ENTRYPOINT ["daux", "generate", "--source=/var/docs", "--destination=/var/static"]
