FROM healthcatalyst/fabric.baseos:latest

LABEL maintainer="Health Catalyst"
LABEL version="2.0"

ENV MIRTH_CONNECT_VERSION 3.5.1.b194

# Install required packages

RUN yum install -y wget krb5-libs krb5-workstation ntp rsync dos2unix; yum clean all

# Install Java
# RUN yum -y install java-1.8.0-openjdk-devel; yum clean all

RUN wget -O jdk.rpm https://fabricnlpfiles.blob.core.windows.net/java/jdk-8u152-linux-x64.rpm \
&& yum install -y ./jdk.rpm \
&& yum clean all \
&& rm -f jdk.rpm

# Install Mirth-Connect
RUN wget -O mirthconnect.rpm http://downloads.mirthcorp.com/connect/$MIRTH_CONNECT_VERSION/mirthconnect-$MIRTH_CONNECT_VERSION-linux.rpm \
&& yum install -y mirthconnect.rpm \
&& yum clean all \
&& rm -f mirthconnect.rpm

# Install Microsoft JDBC Driver
RUN wget -O - https://download.microsoft.com/download/0/2/A/02AAE597-3865-456C-AE7F-613F99F850A8/enu/sqljdbc_6.0.8112.100_enu.tar.gz \
| tar xz \
&& cp sqljdbc_6.0/enu/jre8/sqljdbc42.jar /opt/mirthconnect/custom-lib \
&& rm -rf sqljdbc_6.0 \
; sed -i '/<\/drivers>/ i\ \t<driver class="com.microsoft.sqlserver.jdbc.SQLServerDriver" name="MS SQL Server" template="jdbc:sqlserver://host:port;databaseName=dbname" selectLimit="SELECT TOP 1 * FROM ?" />' /opt/mirthconnect/conf/dbdrivers.xml

# Install RabbitMQ Java Client
RUN wget -O ampq-client.jar  http://central.maven.org/maven2/com/rabbitmq/amqp-client/4.0.2/amqp-client-4.0.2.jar \
&& mv ampq-client.jar /opt/mirthconnect/custom-lib \
&& wget -O slf4j-api.jar http://central.maven.org/maven2/org/slf4j/slf4j-api/1.7.21/slf4j-api-1.7.21.jar \
&& mv slf4j-api.jar /opt/mirthconnect/custom-lib \
&& wget -O slf4j-simple.jar http://central.maven.org/maven2/org/slf4j/slf4j-simple/1.7.22/slf4j-simple-1.7.22.jar \
&& mv slf4j-simple.jar /opt/mirthconnect/custom-lib

ADD mariadb.repo /etc/yum.repos.d/

RUN yum -y install MariaDB-client; yum clean all

ADD conf/mirthconnect/* /opt/mirthconnect/

ADD conf/appdata/* /opt/mirthconnect/appdata/

ADD conf/channels/* /opt/mirthconnect_channels/

ADD conf/database/* /opt/mirthconnect_database/

ADD conf/mysql/* /opt/mirthconnect_mysql/

ADD conf/mirthconnect/mirth.properties /opt/mirthconnect/conf/mirth.properties
ADD conf/mirthconnect/log4j.properties /opt/mirthconnect/conf/log4j.properties
ADD conf/mirthconnect/log4j.properties /opt/mirthconnect/conf/jetty-logging.properties

ADD conf/setenv.sh ./setenv.sh

ADD docker-entrypoint.sh ./docker-entrypoint.sh

RUN dos2unix /opt/mirthconnect/startmirthandrenewcredentials.sh &>/dev/null \
    && chmod +x /opt/mirthconnect/startmirthandrenewcredentials.sh \
    && dos2unix /opt/mirthconnect_channels/deployrealtimechannel.sh &>/dev/null \
    && chmod +x /opt/mirthconnect_channels/deployrealtimechannel.sh \
	&& dos2unix /opt/mirthconnect_database/switchtosqlserver.sh &>/dev/null \
	&& chmod +x /opt/mirthconnect_database/switchtosqlserver.sh \
	&& dos2unix /opt/mirthconnect_mysql/* &>/dev/null \
	&& chmod +x /opt/mirthconnect_mysql/* \
	&& dos2unix /opt/mirthconnect_database/* &>/dev/null \
	&& chmod +x /opt/mirthconnect_database/* \
	&& dos2unix ./setenv.sh &>/dev/null \
	&& chmod +x ./setenv.sh \
	&& dos2unix ./docker-entrypoint.sh &>/dev/null \
	&& chmod +x ./docker-entrypoint.sh

EXPOSE 8080 8443 6661

ENTRYPOINT [ "./docker-entrypoint.sh" ]

# Start Mirth-Connect as a service
CMD ["/opt/mirthconnect/mcservice", "run"]
