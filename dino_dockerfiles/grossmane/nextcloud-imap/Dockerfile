FROM nextcloud:11.0.3
MAINTAINER Jens Grossmann <grossmane@users.noreply.github.com>

#ENV http_proxy http://proxy:8080
#ENV https_proxy http://proxy:8080

RUN apt-get update && apt-get install -y libc-client-dev libkrb5-dev && rm -r /var/lib/apt/lists/*
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap

#ENV http_proxy=""
#ENV https_proxy=""
