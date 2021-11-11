FROM chialab/php:latest
MAINTAINER llamas.jf@gmail.com

# Install PHP IMAP extension
RUN \
    apt-get update && \
    apt-get install -y --no-install-recommends libc-client-dev libkrb5-dev && \
    docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos && \
    docker-php-ext-install imap && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*