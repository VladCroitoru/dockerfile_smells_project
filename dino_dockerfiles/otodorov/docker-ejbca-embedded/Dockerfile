# EJBCA embedded server

FROM centos:centos7.2.1511

# expose
EXPOSE 8080 8442 8443

# declare vars
ENV JBOSS_HOME=/opt/jboss-as-7.1.1.Final \
	APPSRV_HOME=/opt/jboss-as-7.1.1.Final \
	EJBCA_HOME=/opt/ejbca_ce_6_3_1_1 \
    # ebjca configs
	EJBCA_CLI_USER=ejbca \
	EJBCA_CLI_PASSWORD=ejbca \
	EJBCA_KS_PASS=foo123 \
    # ca config
	CA_NAME=ManagementCA \
	CA_DN=CN=ManagementCA,O=EJBCA,C=FR \
	CA_KEYSPEC=2048 \
	CA_KEYTYPE=RSA \
	CA_SIGNALG=SHA256WithRSA \
	CA_VALIDITY=3650 \
    # web config
	WEB_SUPERADMIN=SuperAdmin \
	WEB_JAVA_TRUSTPASSWORD=changeit \
	WEB_HTTP_PASSWORD=serverpwd \
	WEB_HTTP_HOSTNAME=localhost \
	WEB_HTTP_DN=CN=localhost,O=EJBCA,C=FR \
	WEB_SELFREG=true

# add files
ADD [	"jboss-as-7.1.1.Final.tar.gz", \
	"ejbca_ce_6_3_1_1.tar.gz", \
	"mariadb-java-client-1.5.2.jar", \
	"mariadb.repo", \
	"ejbcainit.sh", \
	"jbossinit.sh", \
	"dbinit.sh", \
	"init.sh", \
	"stop.sh", \
	"/opt/"]

# install prereq
RUN rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
	yum install -y net-tools java-1.7.0-openjdk java-1.7.0-openjdk-devel ant ant-optional && \
	groupadd ejbca && useradd ejbca -g ejbca && \
	mv /opt/mariadb.repo /etc/yum.repos.d/ && \
	chmod 750 /opt/init.sh && chmod 750 /opt/stop.sh && chmod 750 /opt/dbinit.sh && chmod 750 /opt/jbossinit.sh && chmod 750 /opt/ejbcainit.sh && \
	# install database
	rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
	yum install -y MariaDB-server MariaDB-client && \
	# jboss
	mkdir -p $JBOSS_HOME/modules/org/mariadb/main/ && \
	mv /opt/mariadb-java-client-1.5.2.jar $JBOSS_HOME/modules/org/mariadb/main/ && \
	sed -i 's/jboss.bind.address.management:127.0.0.1/jboss.bind.address.management:0.0.0.0/' $APPSRV_HOME/standalone/configuration/standalone.xml

CMD ["/opt/init.sh"]
