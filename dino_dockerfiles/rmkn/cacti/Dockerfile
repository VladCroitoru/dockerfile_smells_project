FROM rmkn/php
MAINTAINER rmkn
RUN yum -y install epel-release
RUN yum -y install cacti php-mysql php-snmp php-xml mysql mysql-server

ENV CACTI_VERSION 0.8.8h
ENV PERCONA_MONITORING_VERSION 1.1.6

RUN curl -o /usr/local/src/cacti.tar.gz -SL http://www.cacti.net/downloads/cacti-${CACTI_VERSION}.tar.gz \
	&& tar zxf /usr/local/src/cacti.tar.gz -C /usr/local/src
RUN curl -o /usr/local/src/percona-monitoring-plugins.tar.gz -SL https://www.percona.com/downloads/percona-monitoring-plugins/${PERCONA_MONITORING_VERSION}/percona-monitoring-plugins-${PERCONA_MONITORING_VERSION}.tar.gz \
	&& tar zxf /usr/local/src/percona-monitoring-plugins.tar.gz -C /usr/local/src \
	&& cd /usr/local/src/percona-monitoring-plugins-${PERCONA_MONITORING_VERSION}/cacti/scripts/ \
	&& cp -p ss_get_by_ssh.php ss_get_mysql_stats.php /usr/share/cacti/scripts/ \
	&& ln -s /usr/local/src/percona-monitoring-plugins-1.1.6/cacti/templates /var/www/html/templates

COPY cacti.conf /etc/httpd/conf.d/
COPY cacti.log /var/log/cacti/
COPY entrypoint.sh /

VOLUME /var/lib/mysql/cacti
EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

ENTRYPOINT ["/entrypoint.sh"]
