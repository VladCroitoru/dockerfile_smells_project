FROM reinblau/lamp
MAINTAINER KALRONG <xrb@kalrong.net>

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install php5-curl apt-utils
RUN curl -sS https://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer
WORKDIR /var/www/
RUN apt-get install -y git
RUN git clone https://github.com/Nakiami/mellivora.git
WORKDIR /var/www/mellivora/
RUN composer install
RUN cp /var/www/mellivora/include/config/config.inc.php.example /var/www/mellivora/include/config/config.inc.php
RUN cp /var/www/mellivora/include/config/db.inc.php.example /var/www/mellivora/include/config/db.inc.php
RUN chown -R www-data:www-data /var/www/mellivora/writable/
RUN cp /var/www/mellivora/install/mellivora.apache.conf /etc/apache2/sites-available/mellivora.conf
RUN a2dissite 000-default
RUN a2enmod ssl
RUN a2ensite mellivora
RUN service apache2 restart
RUN echo 'mysql-server mysql-server/root_password password changeme' | debconf-set-selections;\
  echo 'mysql-server mysql-server/root_password_again password changeme' | debconf-set-selections;\
  apt-get install -y mysql-server mysql-client libmysqlclient-dev
RUN service mysql start; echo "CREATE DATABASE mellivora CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -uroot -pchangeme; mysql mellivora -uroot -pchangeme < /var/www/mellivora/install/mellivora.sql; mysql mellivora -uroot -pchangeme < /var/www/mellivora/install/countries.sql; echo "GRANT ALL PRIVILEGES ON mellivora.* To 'root'@'%' IDENTIFIED BY '';" | mysql -uroot -pchangeme
RUN service mysql start; echo "GRANT ALL PRIVILEGES ON mellivora.* To 'root'@'%' IDENTIFIED BY '';" | mysql -uroot -pchangeme
RUN systemctl enable mysql
