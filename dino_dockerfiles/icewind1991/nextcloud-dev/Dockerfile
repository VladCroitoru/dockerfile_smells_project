FROM icewind1991/php-nginx:7
MAINTAINER  Robin Appelman <robin@icewind.nl>
# MAINTAINER Robin Schneider <ypid@riseup.net>
# MAINTAINER silvio <silvio@port1024.net>
# MAINTAINER Josh Chaney <josh@chaney.io>

RUN DEBIAN_FRONTEND=noninteractive ;\
	apt-get update && \
	apt-get install --assume-yes \
		cron \
		redis-server \
		smbclient \
		sudo \
		wget \
		attr \
		git \
        neovim \
        nano
        
RUN wget https://phar.phpunit.de/phpunit-8.phar -O /usr/local/bin/phpunit.phar

ADD configs/autoconfig_mysql.php configs/autoconfig_pgsql.php configs/autoconfig_oci.php configs/s3.php configs/swift.php configs/swiftv3.php configs/azure.php configs/config.php /root/
ADD configs/nginx-app.conf /etc/nginx/

RUN mkdir --parent /var/log/cron
ADD configs/cron.conf /etc/oc-cron.conf
RUN crontab /etc/oc-cron.conf

ADD misc/bootstrap.sh misc/occ misc/tests misc/phpunit misc/install misc/occ misc/integration /usr/local/bin/

ENV WEBROOT /var/www/html

ENTRYPOINT  ["bootstrap.sh"]
