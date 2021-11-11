FROM nouchka/symfony
RUN apt-get update \
    && apt-get -y install imagemagick

RUN usermod -u 1000 www-data \
    && groupmod -g 1000 www-data \
    && usermod -s /bin/bash www-data

COPY index.php /var/www/html/index.php
COPY generate.php /var/www/html/generate.php
