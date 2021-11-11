############################################################
# Dockerfile: CentOS/PHP/Nginx
############################################################
FROM centos:centos6

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

# Default Web Port
ENV WEBPORT 		80
ENV DOMAINNAME 		carbonhost.com

# Add the ngix repository
ADD nginx.repo /etc/yum.repos.d/nginx.repo

# Install nginx 
RUN yum -y install nginx; yum -y clean all

# Install PHP
RUN yum -y install php
RUN yum -y --enablerepo=remi,remi-php56 install nginx php-fpm php-common; yum -y clean all
RUN yum -y --enablerepo=remi,remi-php55 install php-cli php-pear php-pdo php-mysqlnd php-pgsql php-gd php-mbstring php-mcrypt php-xml; yum -y clean all

# Install supervisor
RUN yum install -y python-setuptools; yum -y clean all
RUN easy_install pip 
RUN pip install supervisor && pip install --upgrade Distribute

# Add Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Add Supervisor configuration
COPY supervisord.conf /etc/

# Modify supervisor's require.txt
RUN sed -i "s/meld3 >= 0.6.5/#meld3 >= 0.6.5/g" /usr/lib/python2.6/site-packages/supervisor-3.1.3-py2.6.egg-info/requires.txt

# Insert default php index
COPY index.php /var/www/index.php

# Runs Finalization items
# Add PHP empty log
RUN touch /var/log/php5-fpm.log && \
	# Modify timezone to Asia/Taipei
	sed -i "s/;date.timezone =.*/date.timezone = 'Asia\/Taipei'/g" /etc/php.ini && \
	# Modify Supervisord.conf
	echo -e "\n[include]\nfiles = /etc/supervisor/conf.d/*.conf\n" >> /etc/supervisord.conf && \
	mkdir -p /etc/supervisor/conf.d/ && \
	# Nginx Config Modification
	sed -i "s/CARBON_WEBPORT/${WEBPORT}/g" /etc/nginx/conf.d/default.conf && \
	sed -i "s/CARBON_DOMAINNAME/${DOMAINNAME}/g" /etc/nginx/conf.d/default.conf && \
	# Change timezone to Taipei
	echo y | cp -p /usr/share/zoneinfo/Asia/Taipei /etc/localtime

# Nginx:80
EXPOSE $WEBPORT

# Exec supervisord
CMD ["/usr/bin/supervisord", "-n","-c","/etc/supervisord.conf"]
