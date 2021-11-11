# docker rm -f sugarcrm-mysql
# docker run -d --name sugarcrm-mysql -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=sugarcrm -e MYSQL_USER=sugarcrm -e MYSQL_PASSWORD=123456 mysql
# docker run -d --name sugarcrm -p 80:80 --link sugarcrm-mysql:mysql mwaeckerlin/sugarcrm

FROM ubuntu
MAINTAINER mwaeckerlin

EXPOSE 80
ENV TIMEZONE "Europe/Zurich"

RUN mkdir /sugar
WORKDIR /sugar
RUN apt-get update
RUN apt-get install -y wget unzip apache2 libapache2-mod-php5 php5-curl php5-gd php5-imap php5-json php5-mysqlnd mysql-client
RUN wget -O- -q http://sourceforge.net/projects/sugarcrm/files/latest/download?source=files > sugar.zip
RUN unzip sugar.zip
RUN rm sugar.zip
RUN mv * crm
RUN sed -i 's,DocumentRoot.*,DocumentRoot /sugar/crm,' /etc/apache2/sites-available/000-default.conf
RUN sed -i 's,;*\(date.timezone *=\).*,\1 "'${TIMEZONE}'",g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(display_errors *=\).*,\1 Off,g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(mbstring.func_overload *=\).*,\1 0,g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(post_max_size *=\).*,\1 100M,g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(session.use_cookies *=\).*,\1 1,g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(upload_max_filesize *=\).*,\1 100M,g' /etc/php5/apache2/php.ini
RUN sed -i 's,;*\(session.gc_maxlifetime *=\).*,\1 14400,g' /etc/php5/apache2/php.ini
RUN bash -c "chown www-data.www-data crm/{.htaccess,config.php,config_override.php,sugarcrm.log}"
RUN bash -c "chown -R www-data.www-data crm/{cache,custom,data,modules,upload}"
RUN ( echo "<Directory /sugar/crm>"; \
      echo "  Options Indexes FollowSymLinks" ;\
      echo "  AllowOverride All"; \
      echo "  Require all granted"; \
      echo "</Directory>"; \
    ) > /etc/apache2/conf-available/sugarcrm.conf
RUN a2enconf sugarcrm
RUN php5enmod curl imap mysql mysqlnd pdo readline gd json mysqli opcache pdo_mysql
RUN echo '*    *    *    *    *     cd /sugar/crm; php -f cron.php > /dev/null 2>&1' > /etc/cron.d/sugar

CMD sed -i 's,;*\(date.timezone *=\).*,\1 "'${TIMEZONE}'",g' /etc/php5/apache2/php.ini \
    && cron && apache2ctl -DFOREGROUND
VOLUME /sugar
