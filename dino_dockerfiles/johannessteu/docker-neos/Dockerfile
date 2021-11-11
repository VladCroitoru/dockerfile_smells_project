FROM johannessteu/docker-nginx-php7:latest
MAINTAINER Johannes Steu <js@johannessteu.de>

# Install packages
RUN apt update

RUN apt-get install -y \
    curl bash less mysql-client ca-certificates openssh-client openssl

RUN apt-cache search php

RUN apt-get install -y \
    php-mysql php-mysqlnd php-mysqli php-sqlite3 php-sqlite3 \
    php-common  php-json php-xml php-pdo php-zip unzip php-imagick \
    php-gd php-curl php-opcache php-ctype php-mbstring php-soap \
    php-intl php-bcmath php-dom php-xmlreader php-phar

ADD /container-files/etc /etc