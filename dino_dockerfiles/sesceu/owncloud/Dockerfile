FROM owncloud:10
MAINTAINER Sebastian Schneider <mail@sesc.eu>

# install cron
RUN apt-get update && apt-get install -y \
        cron \
        libc-client2007e-dev \
        libkrb5-dev \
        && rm -rf /var/lib/apt/lists/* \
        && update-rc.d cron defaults 


# configure cron to run every 15min
RUN echo "SHELL=/bin/bash" >> /etc/cron.d/owncloud-cron \
    && echo "PATH=/usr/local/bin:/usr/bin:/bin" >> /etc/cron.d/owncloud-cron \
    && echo "# m h	dom	mon	dow user		command" >> /etc/cron.d/owncloud-cron \
    && echo "*/15	*	*	*	*	www-data	php -f /var/www/html/cron.php > /dev/null 2>&1" >> /etc/cron.d/owncloud-cron

# install php5-imap
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl \
    && docker-php-ext-install imap \
    && docker-php-ext-enable imap

CMD /etc/init.d/cron start; apache2-foreground
