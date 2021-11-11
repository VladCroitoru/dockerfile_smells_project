FROM fathershawn/front-end:codeship
LABEL maintainer="fathershawn"


RUN addgroup -g 82 -S www-data \
  && adduser -u 82 -D -S -G www-data www-data \
  && chmod ugo=rx /usr/local/bin/entrypoint.sh

RUN mkdir /var/www && chown -R www-data:www-data /var/www

VOLUME /var/www

ENTRYPOINT ["entrypoint.sh"]

USER www-data
