FROM tonisormisson/dev-lemp:0.7.1
ENV DEBIAN_FRONTEND noninteractive

# start mysql
RUN find /var/lib/mysql -type f -exec touch {} \; && service mysql start

## nginx conf
COPY nginx/default /etc/nginx/sites-available/default

# start things
RUN service php7.4-fpm start
RUN service nginx restart

## copy limesurvey
RUN rm -rf /var/www/html/*
ADD html/ /var/www/html/


# set lime permissions
RUN cd /var/www/html/ && chown -R 1000:www-data tmp
RUN cd /var/www/html/ && chown -R 1000:www-data upload
RUN cd /var/www/html/ && chown -R 1000:www-data tests/tmp


# install Limesurvey
RUN cd /var/www/html/ && composer install
RUN cd /var/www/html/ && cp application/config/config-sample-mysql.php application/config/config.php
RUN cd /var/www/html/ && sed -i "s/'password' => ''/'password' => 'root'/"  application/config/config.php
RUN cd /var/www/html/ && sed -i "s/'debug'=>0,/'debug'=>2,'maxLoginAttempt' => 999999999,/"  application/config/config.php

RUN cd /var/www/html/ && chmod -R 775 tmp
RUN cd /var/www/html/ && chmod -R 775 upload
RUN cd /var/www/html/ && chmod -R 775 tests/tmp


## enable json RPC
RUN cd /var/www/html/ && sed -i "/Update default LimeSurvey config here/a \ \ \ \ \ \ \ \ 'RPCInterface' => 'json', " application/config/config.php
RUN service mysql start && cd /var/www/html/ && php application/commands/console.php install admin password TravisLS no@email.com verbose


# Expose Ports
EXPOSE 443
EXPOSE 80
EXPOSE 3306
COPY start.sh /start.sh
RUN chmod a+x /start.sh
RUN ls -lst

## cleanup of files from setup
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /var/www/html

CMD sh /start.sh
ENV DEBIAN_FRONTEND teletype
