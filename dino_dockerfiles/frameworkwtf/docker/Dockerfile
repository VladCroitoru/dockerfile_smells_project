FROM alpine:latest

ENV PHP_OPCACHE_ENABLE 0
# Workaround https://bugs.php.net/bug.php?id=71880
ENV LOG_STREAM /tmp/log
ENV NGINX_ENABLE 1
ENV CRON_ENABLE 1

ENV APP_DIR /var/www
ENV APP_ENV dev
ENV APP_RELEASE local
ENV APP_HOST localhost
ENV APP_SECRET qwerty

RUN apk --no-cache add nginx php7 php7-fpm php7-json php7-ctype php7-mbstring php7-curl php7-opcache php7-session && \
    mkfifo $LOG_STREAM && chmod 777 $LOG_STREAM

COPY ./etc /etc
COPY ./usr /usr

RUN chmod +x /usr/bin/*

VOLUME $APP_DIR
WORKDIR $APP_DIR

EXPOSE 8080 9000

CMD ["entrypoint"]
