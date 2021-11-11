# vim:set ft=dockerfile:
FROM centos:6

MAINTAINER "Kentaro Ohkouchi" <nanasess@fsm.ne.jp>

### see also https://github.com/docker-library/mysql/blob/8b08921b27f9505f738cc61c551e776815e50d5b/5.5/Dockerfile

# explicitly set user/group IDs
RUN groupadd -r mysql && useradd -r -g mysql mysql

ENV GOSU_VERSION 1.7
RUN gpg --keyserver pgp.mit.edu --recv-keys \
	B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& curl -sSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64 -o /bin/gosu \
	&& chmod +x /bin/gosu \
	&& curl -sSL https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-amd64.asc -o /tmp/gosu.asc \
	&& gpg --verify /tmp/gosu.asc /bin/gosu \
	&& rm /tmp/gosu.asc

ENV LANG en_US.utf8

RUN mkdir /docker-entrypoint-initdb.d

ENV MYSQL_MAJOR 5.1
ENV MYSQL_VERSION 5.1.73

RUN yum -y update \
        && yum -y install wget binutils \
        && wget "http://dev.mysql.com/get/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION-linux-x86_64-glibc23.tar.gz" -O mysql.tar.gz \
        && wget "http://mysql.he.net/Downloads/MySQL-$MYSQL_MAJOR/mysql-$MYSQL_VERSION-linux-x86_64-glibc23.tar.gz.asc" -O mysql.tar.gz.asc \
	&& export GNUPGHOME="$(mktemp -d)" \
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A4A9406876FCBD3C456770C88C718D3B5072E1F5 \
	&& gpg --batch --verify mysql.tar.gz.asc mysql.tar.gz \
	&& rm -r "$GNUPGHOME" mysql.tar.gz.asc \
	&& mkdir /usr/local/mysql \
	&& tar -xzf mysql.tar.gz -C /usr/local/mysql --strip-components=1 \
	&& rm mysql.tar.gz \
	&& rm -rf /usr/local/mysql/mysql-test /usr/local/mysql/sql-bench \
	&& rm -rf /usr/local/mysql/bin/*-debug /usr/local/mysql/bin/*_embedded \
	&& find /usr/local/mysql -type f -name "*.a" -delete \
	&& { find /usr/local/mysql -type f -executable -exec strip --strip-all '{}' + || true; }
ENV PATH $PATH:/usr/local/mysql/bin:/usr/local/mysql/scripts

RUN mkdir -p /etc/mysql/conf.d \
	&& { \
		echo '[mysqld]'; \
		echo 'skip-host-cache'; \
		echo 'skip-name-resolve'; \
		echo 'datadir = /var/lib/mysql'; \
		echo '!includedir /etc/mysql/conf.d/'; \
	} > /etc/mysql/my.cnf

RUN mkdir -p /var/lib/mysql /var/run/mysqld \
	&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
# ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime
	&& chmod 777 /var/run/mysqld

ENV PATH $PATH:/usr/local/bin:/usr/local/mysql/bin:/usr/local/mysql/scripts

VOLUME /var/lib/mysql
WORKDIR /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306
CMD ["mysqld", "--datadir=/var/lib/mysql", "--user=mysql"]
