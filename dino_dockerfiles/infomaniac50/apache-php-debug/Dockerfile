FROM tutum/apache-php

RUN a2enmod rewrite
RUN apt-get update && apt-get -y install php5-xdebug
RUN echo "xdebug.remote_enable=1\nxdebug.remote_handler=dbgp\nxdebug.remote_mode=req\nxdebug.remote_host=127.0.0.1\nxdebug.remote_port=9000" >> "/etc/php5/mods-available/xdebug.ini"
RUN echo "<Directory /var/www/html/>\nOptions Indexes FollowSymLinks\nAllowOverride All\nRequire all granted\n</Directory>" >> /etc/apache2/apache2.conf

EXPOSE 9000


