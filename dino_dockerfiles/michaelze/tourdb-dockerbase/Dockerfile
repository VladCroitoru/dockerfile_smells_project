FROM debian:wheezy
MAINTAINER Michael Zender <michael@crazymonkeys.de>

RUN DEBIAN_FRONTEND=noninteractive apt-get update -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git apache2 libapache2-mod-php5 php5-mysql locales
RUN DEBIAN_FRONTEND=noninteractive apt-get clean

RUN sed -ir "s/# de_DE.UTF-8 UTF-8/de_DE.UTF-8 UTF-8/" /etc/locale.gen
RUN sed -ir "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen
RUN echo "en_US.UTF-8 UTF-8" >> /etc/default/locale
RUN locale-gen

RUN a2enmod rewrite
RUN a2enmod expires

RUN sed -ir "s/variables_order\s*=.*/variables_order = \"EGPCS\"/" /etc/php5/apache2/php.ini
RUN sed -ir "s/variables_order\s*=.*/variables_order = \"EGPCS\"/" /etc/php5/cli/php.ini
RUN sed -ir "s/upload_max_filesize\s*=.*/upload_max_filesize = 6M/" /etc/php5/apache2/php.ini

RUN git clone https://github.com/cakephp/cakephp /var/tourdb_cakephp
RUN cd /var/tourdb_cakephp && git checkout 1.3.11
# Patch CakePHP console entrypoint to suppress strict warnings when running shell scripts
RUN sed -ir "s/error_reporting.*/error_reporting', E_ALL \& ~E_DEPRECATED \& ~E_STRICT);/" /var/tourdb_cakephp/cake/console/cake.php

RUN mkdir -p /var/tourdb_pear
RUN git clone https://github.com/PHPOffice/PHPExcel.git /usr/local/lib/PHPExcel
RUN cd /usr/local/lib/PHPExcel && git checkout 1.7.9
RUN ln -s /usr/local/lib/PHPExcel/Classes /var/tourdb_pear/PHPExcel

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

EXPOSE 80

CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]