FROM mysql:5.6

MAINTAINER weiboyi lijie1@weiboyi.com

COPY ./devbox.cnf /etc/mysql/mysql.conf.d/

COPY docker-entrypoint.sh /usr/local/bin/

VOLUME /var/lib/mysql

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306

CMD ["mysqld"]
