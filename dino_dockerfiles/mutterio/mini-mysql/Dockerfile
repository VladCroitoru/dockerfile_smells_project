FROM mutterio/mini-base

ENV MYSQL_VERSION 5.5.43-r4

RUN apk-install mysql=$MYSQL_VERSION mysql-client=$MYSQL_VERSION pwgen

ADD ./config/mysql.conf /etc/mysql/my.cnf
ADD ./scripts/start.sh /start.sh

VOLUME ["/data"]

EXPOSE 3306

CMD ["/start.sh"]
