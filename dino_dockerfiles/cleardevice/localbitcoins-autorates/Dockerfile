FROM alpine:3.3
MAINTAINER cd "cleardevice@gmail.com"

ADD ./ /lbtc
ADD ./profile /root/.profile
RUN apk add --no-cache php-cli php-curl php-json php-phar php-openssl ca-certificates nano && \
    apk add --no-cache grc --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ && \
    cd /lbtc && curl -O https://getcomposer.org/composer.phar && chmod +x ./composer.phar && ./composer.phar update

WORKDIR /root
ENV ENV /root/.profile
ENV PATH $PATH:/lbtc/bin:/lbtc/bin/rub:/lbtc/bin/usd:/lbtc/bin/uah

CMD ["/bin/ash", "true"]
