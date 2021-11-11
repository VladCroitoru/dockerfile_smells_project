FROM centos:centos7
ENV PACKAGE_URL https://repo.mysql.com/yum/mysql-5.7-community/docker/x86_64/mysql-community-server-minimal-5.7.12-1.el7.x86_64.rpm

# Install server 
RUN rpmkeys --import http://repo.mysql.com/RPM-GPG-KEY-mysql \
  && yum install -y $PACKAGE_URL \
  && yum install -y libpwquality \
  && rm -rf /var/cache/yum/* 

RUN mkdir -p /var/lib/mysql/data \
        && chmod -R 777 /var/lib/mysql \
	&& chown -R mysql:mysql /var/lib/mysql

RUN mkdir /docker-entrypoint-initdb.d

COPY docker-entrypoint.sh /entrypoint.sh

RUN chown -R mysql:mysql /entrypoint.sh \
    && chmod -R 777 /entrypoint.sh \
    && chmod +x /entrypoint.sh

USER mysql

EXPOSE 3306

VOLUME ["/var/lib/mysql/data"]

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld", "--datadir=/var/lib/mysql/data"]

