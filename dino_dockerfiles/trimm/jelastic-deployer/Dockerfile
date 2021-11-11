FROM composer/composer:alpine
MAINTAINER Mark Wienk <mark.wienk@trimm.nl>
ADD . /jelastic
WORKDIR /jelastic
RUN composer self-update && composer install
ENV PATH="/jelastic/bin:${PATH}"
CMD ["console"]
ENTRYPOINT []
