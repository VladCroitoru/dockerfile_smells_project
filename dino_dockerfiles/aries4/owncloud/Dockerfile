FROM		ubuntu:14.04
MAINTAINER	aries4

ADD         bootstrap.sh /usr/bin/

RUN         sh -c "echo 'deb http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/owncloud.list"
RUN			apt-get update && \
            apt-get install -y --force-yes owncloud wget supervisor
RUN			cd /root
RUN			wget http://download.opensuse.org/repositories/isv:ownCloud:community/xUbuntu_14.04/Release.key
RUN			apt-key add - < Release.key  

RUN        	chown -R www-data:www-data /var/www/owncloud && \
            chmod +x /usr/bin/bootstrap.sh

ADD         cron.conf /etc/oc-cron.conf
RUN         crontab /etc/oc-cron.conf


EXPOSE      80
EXPOSE      443

RUN 		mkdir -p /var/log/supervisor
ADD 		supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD			autoconfig.php /var/www/owncloud/config/autoconfig.php
CMD ["/bin/bash", "-e", "/usr/bin/bootstrap.sh"]
