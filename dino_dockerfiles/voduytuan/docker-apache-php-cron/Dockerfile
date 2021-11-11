FROM voduytuan/docker-apache-php:latest

#override start.sh from docker-apache-php, with add cron command
ADD start.sh /start.sh

ADD crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab

ADD crontab.sh /var/www/crontab.sh
RUN chmod 0755 /var/www/crontab.sh

ADD cronjob.php /var/www/site/cronjob.php
RUN chmod 0755 /var/www/site/cronjob.php



