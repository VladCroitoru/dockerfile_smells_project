FROM composer:2.1.11 as builder

COPY . /app

WORKDIR /app/

RUN composer install --no-dev -a

FROM alpine:3.14.2

RUN apk add --no-cache php7 php7-openssl php7-dom php7-simplexml php7-xmlreader ca-certificates

WORKDIR /app/

COPY --from=builder /app .

CMD [ "sh", "/app/help.sh" ]
