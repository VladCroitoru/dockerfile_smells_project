FROM tutum/apache-php
RUN apt-get update && apt-get install -yq git php-zeroc-ice && rm -rf /var/lib/apt/lists/*
RUN rm -fr /app
ADD . /app
ADD IcePHP.ini /etc/php5/mods-available/IcePHP.ini
RUN php5enmod IcePHP
#RUN composer install
