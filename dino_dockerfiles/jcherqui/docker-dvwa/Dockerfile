FROM tutum/lamp:latest

RUN rm -fr /app && git clone https://github.com/RandomStorm/DVWA /app
RUN sed -i -e "s/AllowOverride FileInfo/AllowOverride FileInfo Options/" /etc/apache2/sites-enabled/000-default.conf
RUN sed -i -e "s/allow_url_include = Off/allow_url_include = On/" /etc/php5/apache2/php.ini
RUN sed -i -e 's/root/admin/' /app/config/config.inc.php
RUN chmod 777 /app/hackable/uploads
RUN chmod 777 /app/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt
RUN apt-get update --fix-missing
RUN apt-get install -y php5-gd vim

EXPOSE 80 3306

CMD ["/run.sh"]

