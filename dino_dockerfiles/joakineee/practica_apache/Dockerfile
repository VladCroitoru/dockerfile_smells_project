FROM debian


RUN apt-get update && apt-get install -y \

        #Installting apache
        apache2 \
        apache2-doc && \
        # Configuring user directories for Apache Web Server
        #Install php
        apt-get install -y \
        php5 \
        php5-mysql \
        libapache2-mod-php5 && \
        #phpmyadmin && \
        apt-get clean && \
        ln -sf /dev/stdout /var/log/apache2/access.log && \
        ln -sf /dev/stderr  /var/log/apache2/error.log

ENTRYPOINT ["/usr/sbin/apachectl", "-D FOREGROUND"]
EXPOSE 80
