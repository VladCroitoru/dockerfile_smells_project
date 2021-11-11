FROM php:8.0-fpm

WORKDIR /app

ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod +x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions pdo_mysql bcmath pcntl zip gd imagick

RUN apt-get update -y && apt-get install -y sendmail unzip

ARG HOST_USER_ID=1000
ARG HOST_GROUP_ID=1000

ENV HOST_USER_ID=$HOST_USER_ID
ENV HOST_GROUP_ID=$HOST_GROUP_ID

RUN \
  if [ $(getent group ${HOST_GROUP_ID}) ]; then \
    useradd  -r -u ${HOST_USER_ID} dockeruser; \
  else \
    groupadd -g ${HOST_GROUP_ID} dockergroup && \
    useradd -r -u ${HOST_USER_ID} -g dockergroup dockeruser; \
  fi

RUN curl -sS https://getcomposer.org/installer | \
  php -- --install-dir=/usr/local/bin --filename=composer

COPY . .

RUN composer install

RUN mkdir -p /home/dockeruser \
  && chown -R dockeruser:dockergroup /home/dockeruser

RUN chown -R dockeruser:dockergroup /app

USER dockeruser

CMD ["php-fpm"]
