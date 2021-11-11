
FROM tutum/lamp

RUN apt-get install -q -y curl php5-gd php5-ldap php5-imap unzip; apt-get clean ; \
	php5enmod imap

RUN rm -rf /app; \
	mkdir -p /app; \
	curl -L -o /app/limesurvey192.zip  http://www.limesurvey.org/en/archived-releases/finish/24-archived-releases/992-limesurvey192plus-build120919-zip ; \
	unzip /app/limesurvey192.zip ; \
	mv  /app/limesurvey/* /app/ ; \
	mv  /app/limesurvey/.* /app/ ; \
	rmdir  /app/limesurvey ; \
	chown -R www-data:www-data /app

RUN chown www-data:www-data /var/lib/php5

EXPOSE 80 3306

CMD ["/run.sh"]
