FROM php:5.6-apache
ENV TERM xterm
RUN apt-get update && apt-get install -y \
    wget \
    git \
    unzip \
    nano && rm -rf /var/lib/apt/lists/*

ADD index.php /var/www/html/


