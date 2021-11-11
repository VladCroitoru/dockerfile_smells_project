FROM php:apache
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y supervisor mariadb-server git libicu-dev libwebp-dev libjpeg-dev libpng-dev libxpm-dev zip
RUN docker-php-ext-install gd intl pdo_mysql
RUN echo 'pdo_mysql.default_socket = "/var/run/mysqld/mysqld.sock"' >>/usr/local/etc/php/conf.d/docker-php-ext-pdo_mysql.ini
RUN a2enmod rewrite
RUN sed -i 's#DocumentRoot /var/www/html#DocumentRoot /var/www/html/web#g' /etc/apache2/sites-enabled/000-default.conf 

RUN mkdir -p /var/www/html/web
WORKDIR /var/www/html/web
RUN curl -so contao-manager.php https://download.contao.org/contao-manager.phar
RUN chown -R www-data:www-data /var/www/html

## contao installation via compose
#WORKDIR /usr/local/bin
#RUN wget -q https://getcomposer.org/composer.phar
#RUN php composer.phar create-project contao/managed-edition /var/www/html

# mysql preparation
RUN mysqld_safe & until mysqladmin ping 2>/dev/null; do sleep 1; done && \
    mysql -uroot -e "CREATE DATABASE contao;" && \
    mysql -uroot -e "CREATE USER 'contao'@'localhost' IDENTIFIED BY 'contao';" && \
    mysql -uroot -e "GRANT ALL PRIVILEGES ON contao.* TO 'contao'@'localhost';"

RUN echo "[mysqld]" >>/etc/mysql/conf.d/mariadb.cnf
RUN echo "innodb_large_prefix = ON" >>/etc/mysql/conf.d/mariadb.cnf
RUN echo "innodb_file_format = Barracuda" >>/etc/mysql/conf.d/mariadb.cnf
RUN echo "innodb_file_per_table = 1" >>/etc/mysql/conf.d/mariadb.cnf

RUN echo "[program:mysqld]\ncommand=mysqld">/etc/supervisor/conf.d/mysql.conf
RUN echo "[program:apache]\ncommand=apache2-foreground">/etc/supervisor/conf.d/apache.conf

VOLUME /var/lib/mysql

CMD ["supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]
