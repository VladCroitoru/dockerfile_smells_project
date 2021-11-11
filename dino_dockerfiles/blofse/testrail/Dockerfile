FROM ubuntu:trusty

ENV IONCUBE_VERSION=6.0.9

RUN apt-get update
RUN apt-get install -y --no-install-recommends php5 php5-cli php5-mysql php5-curl curl unzip
RUN rm -rf /var/lib/apt/lists/*

COPY testrail-*.zip /
COPY run.sh /

RUN curl -O http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64_${IONCUBE_VERSION}.tar.gz \
   && tar vxfz ioncube_loaders_lin_x86-64_${IONCUBE_VERSION}.tar.gz \
   && rm -f ioncube_loaders_lin_x86-64_${IONCUBE_VERSION}.tar.gz \
   && sed -i 's~;zend.script_encoding\ =~zend_extension=/ioncube/ioncube_loader_lin_5.5.so~' /etc/php5/cli/php.ini \
   && sed -i 's~;zend.script_encoding\ =~zend_extension=/ioncube/ioncube_loader_lin_5.5.so~' /etc/php5/apache2/php.ini \
   && cd /var/www/html && unzip -q /testrail-*.zip \
   && mkdir /var/www/html/testrail/logs \
   && chown www-data /var/www/html/testrail/logs \
   && echo '* * * * * www-data /usr/bin/php /var/www/html/testrail/task.php' > /etc/cron.d/testrail \
   && chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
