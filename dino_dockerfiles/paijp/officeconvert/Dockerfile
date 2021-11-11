FROM paijp/centos6-apache-php-sqlite2

RUN \
	set -x &&\
	yum install -y libreoffice-headless libreoffice-calc libreoffice-writer libreoffice-impress

RUN \
	set -x &&\
	yum install -y libreoffice-langpack-ja

RUN \
	set -x &&\
	mkdir -p /var/www/html/work &&\
	chown apache:apache /var/www/html/work

ADD index.php /var/www/html/

EXPOSE 80
CMD apachectl start&&tail -f /var/log/httpd/access_log
