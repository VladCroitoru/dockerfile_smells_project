############################################################
# Dockerfile: CentOS6/MySQL
# Pure MySQL DB Application with default user
############################################################

FROM centos:centos6

MAINTAINER CarbonSphere <CarbonSphere@gmail.com>

ENV HOME 						/root
ENV TERM 						xterm

# Install MySQL
RUN yum -y install mysql-server mysql-client; \
    yum -y update; \
	yum -y clean all;

# Add Environment Variables
ENV MYSQL_USER				carbon
ENV MYSQL_PASS 				carbon
ENV MYSQL_ROOT_PASSWORD 	carbon
ENV MYSQL_PORT				3306
ENV MYSQL_ID				1
ENV MYSQL_SLAVE_USER		carbonSlave
ENV MYSQL_SLAVE_PASS		DEFAULT
ENV MYSQL_MASTER_HOST		DEFAULT
ENV MYSQL_MASTER_USER		carbonSlave
ENV MYSQL_MASTER_PASS		DEFAULT
ENV MYSQL_SSL_PATH		/ssl
ENV MYSQL_SSL_CA		ca.pem
ENV MYSQL_SSL_CERT		server.pem
ENV MYSQL_SSL_KEY		server.key		

# Add create user & db script to root
ADD createUserDb.sh /usr/local/bin/createUserDb.sh
ADD start.sh /usr/local/bin/start.sh
ADD test-ssl.sh /usr/local/bin/test-ssl.sh

# Install MySQL
RUN echo -e "\nsocket=/var/lib/mysql/mysql.sock" >> /etc/my.cfg; \
	/bin/sed -i "s/\[mysqld\]/\[mysqld\]\nbind-address = 0.0.0.0\nserver-id = 1\nlog-bin = mysql-bin\nbinlog-ignore-db=\"mysql\"\n#master-host\n#master-user\n#master-password\n#master-connect-retry\nlog-slave-updates = 1\n#ssl-ca\n#ssl-cert\n#ssl-key/" /etc/my.cnf

# MySQL : $MYSQL_PORT
EXPOSE $MYSQL_PORT

# Start MySQL
RUN service mysqld start && \
	sleep 5 && \
    /usr/bin/mysqladmin -u root password ${MYSQL_ROOT_PASSWORD} && \
    # Move MySQL script to run command in docker file \
	mysql -uroot -p${MYSQL_ROOT_PASSWORD} -e "CREATE USER '${MYSQL_USER}' IDENTIFIED BY '${MYSQL_PASS}'; \
		REVOKE ALL PRIVILEGES,GRANT OPTION from ${MYSQL_USER}; \
		GRANT USAGE ON *.* to '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASS}'; \
		GRANT ALL PRIVILEGES ON *.* TO '${MYSQL_USER}'@'%' WITH GRANT OPTION; \
		DROP USER ''@'localhost'; \
		DROP USER ''@'$(hostname)'; \
		DROP DATABASE test; \
		FLUSH PRIVILEGES; \
		reset master;"

CMD ["start.sh"]
