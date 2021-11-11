FROM ubuntu:14.04
MAINTAINER Grant Hutchinson <h.g.utchinson@gmail.com>

ADD ./modules /var/www/html/site/sites/all/modules
ADD ./themes /var/www/html/site/sites/all/themes
ADD ./bootup.sh /root/bootup.sh
ADD ./.git    /var/www/html/site/sites/all/.git
ADD ./.gitmodules /var/www/html/site/sites/all/.gitmodules

RUN apt-get update && \
    apt-get install -y apache2 mysql-client php5 php5-mysql php5-curl php5-gd curl wget git && \
	cd /var/www/html/site && wget http://ftp.drupal.org/files/projects/drupal-7.35.tar.gz && \
	tar -zxvf ./drupal*.tar.gz && \
	cp ./drupal*/*  . -r  && cp ./drupal*/.htaccess ./.htaccess && \
	mkdir ./sites/default/files  && \
	cp ./sites/default/default.settings.php ./sites/default/settings.php && \
	cd .. && chmod 755 ./site -R && cd /var/www/html/site/sites/default && \
	chmod 777 ./settings.php && chmod 777 ./files && \
	rm -r /var/www/html/site/drupal* && \
	cd /var/www/html/site/sites/all && git submodule init && git submodule update && \
	rm -f ./.git -R && rm ./.gitmodules && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80
CMD ["/bin/bash", "/root/bootup.sh"]
