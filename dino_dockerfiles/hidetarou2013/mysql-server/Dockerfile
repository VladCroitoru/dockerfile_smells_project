FROM mysql
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

RUN { \
    echo '[mysqld]'; \
    echo 'character-set-server=utf8'; \
    echo 'collation-server=utf8_general_ci'; \
    echo '[client]'; \
    echo 'default-character-set=utf8'; \
} > /etc/mysql/conf.d/charset.cnf

#CMD service mysql start
CMD ["mysqld"]
