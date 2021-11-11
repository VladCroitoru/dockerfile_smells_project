FROM centos
MAINTAINER Miguel Vargas <puntadelanza86@gmail.com>

RUN yum -y update && yum -y install httpd php php-devel php-mysqlnd gcc libtool git make php-pgsql

WORKDIR /tmp

RUN git clone --depth=1 git://github.com/phalcon/cphalcon.git && \
	cd cphalcon/build/ && \
	./install && \
	rm -rf /tmp/cphalcon && \
	echo 'extension=phalcon.so' > /etc/php.d/phalcon.ini

WORKDIR /var/www/html/app

RUN echo '<?php phpinfo();' > /var/www/html/app/no.php

EXPOSE 80

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
