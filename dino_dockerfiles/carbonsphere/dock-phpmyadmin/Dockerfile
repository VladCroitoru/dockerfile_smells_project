############################################################
# Dockerfile: CentOS6/PHP/PHPMyAdmin
# Based on "carbonsphere/docker-centos6-php-nginx"
# PHPMyAdmin Web Application for managing DB container
############################################################
FROM carbonsphere/docker-centos6-php-nginx

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

ENV DBNAME	DB
ENV DBPORT	3306

# Install PHP
RUN yum -y --enablerepo=remi,remi-php56 install php php-cli php-pear php-pdo php-mysqlnd php-pgsql php-gd php-mbstring php-mcrypt php-xml; yum -y clean all

# Add EPEL Release
RUN yum -y install epel-release; yum -y install phpmyadmin; yum -y clean all

# Add Environment variable work around shell script
COPY env.sh /root/env.sh

# add phpmyadmin softlink to web directory
RUN ln -s /usr/share/phpMyAdmin /var/www; mv /var/www/index.php /var/www/phpinfo.php; \
	# Add new index.php to redirect to phpMyAdmin
	echo -e "<?php\nheader('Location: /phpMyAdmin/index.php');\n?>" > /var/www/index.php; \
	env | grep _ENV_MYSQL_ROOT_PASSWORD= | sed "s/_ENV_MYSQL_ROOT_PASSWORD=.*//g"; \
	# Configure phpMyAdmin
	sed -i "s/\$cfg\['Servers'\]\[\$i\]\['host'\].*/\$cfg\['Servers'\]\[\$i\]\['host'\]          \
	= getEnv("DBNAME")?getEnv("DBNAME"):\"DB\";/g" /etc/phpMyAdmin/config.inc.php; \
	sed -i "s/\$cfg\['Servers'\]\[\$i\]\['port'\].*/\$cfg\['Servers'\]\[\$i\]\['port'\]          \
	= getEnv("DBPORT")?getEnv("DBPORT"):3306;/g" /etc/phpMyAdmin/config.inc.php; \
	chmod +x /root/env.sh

# Run Environmnet variable first before running supervisord
CMD /root/env.sh && /usr/bin/supervisord -n -c /etc/supervisord.conf


