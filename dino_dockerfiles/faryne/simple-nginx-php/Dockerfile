# dockerfile 基本資訊
FROM ubuntu:18.04
MAINTAINER Faryne <faryne@gmail.com>

# 設定開啟的 port 
EXPOSE 80 443

# 設定環境變數
ENV VERSION 0.0.10
ENV TZ 'Asia/Taipei'

# 設定時區資訊等，避免建置時 hang 住沒辦法運作
RUN echo $TZ > /etc/timezone && \
  apt-get update && apt-get install -y tzdata && \
  rm /etc/localtime && \
  ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
  dpkg-reconfigure -f noninteractive tzdata && \
  apt-get clean

# 安裝 nginx / git / wget / php7.2 等
RUN apt-get install -y \
        nginx git wget php7.2-common php7.2-fpm php7.2-cli \
        php7.2-mysql php7.2-mbstring php7.2-curl php7.2-zip \
        php7.2-gd php7.2-json php7.2-odbc php7.2-soap php7.2-bcmath 

# 裝好 composer 套件
RUN wget https://getcomposer.org/download/1.6.5/composer.phar -O composer && \ 
    chmod +x composer && \
    mv composer /usr/local/bin/composer 

# 設定預設頁面
RUN echo "Hello World (By simple-nginx-php $VERSION). See https://github.com/faryne/simple-nginx-php for more info." > /var/www/html/index.html
RUN echo "<?php phpinfo();?><p><small>Hello World (By simple-nginx-php $VERSION). See https://github.com/faryne/simple-nginx-php for more info.</small></p>" > /var/www/html/index.php

# 複製 nginx / php 設定檔
COPY ./conf/nginx/nginx.conf /etc/nginx
COPY ./conf/nginx/virtual_hosts/default /etc/nginx/sites-available
COPY ./conf/php/cli/php.ini /etc/php/7.2/cli
COPY ./conf/php/fpm/php.ini /etc/php/7.2/fpm
COPY ./conf/php/fpm/php-fpm.conf /etc/php/7.2/fpm

# 設定開機後（？）要啟動的服務，但是寫 ENTRYPOINT / CMD 好像都會出錯導致 container 跑不起來
# 只好先把檔案複製過去，啟動後再手動執行 
#WORKDIR /
#COPY ./start.sh /
#RUN chmod 0755 /start.sh 
#ENTRYPOINT bash -C '/start.sh'; bash
