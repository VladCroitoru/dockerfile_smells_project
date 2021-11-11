#
# Activiti Dockerfile
#
FROM podbox/tomcat8
MAINTAINER Jan Boonen "jan.boonen@geodan.nl"

EXPOSE 8080

ENV ACTIVITI_VERSION 6.0.0.Beta1
ENV MYSQL_CONNECTOR_JAVA_VERSION 5.1.36
ENV POSTGRESQL_DRIVER_VERSION 9.4-1201.jdbc41

RUN apt-get install -y unzip wget

# Fetch and explode distributions
RUN \
  wget https://github.com/Activiti/Activiti/releases/download/activiti-${ACTIVITI_VERSION}/activiti-${ACTIVITI_VERSION}.zip -O /tmp/activiti.zip -nv && \
  unzip -q /tmp/activiti.zip -d /activiti && \
  unzip -q /activiti/activiti-${ACTIVITI_VERSION}/wars/activiti-app.war -d /apache-tomcat/webapps/activiti-app && \
  unzip -q /activiti/activiti-${ACTIVITI_VERSION}/wars/activiti-rest.war -d /apache-tomcat/webapps/activiti-rest

# MySQL
RUN \
  wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_CONNECTOR_JAVA_VERSION}.zip -O /tmp/mysql-connector-java.zip -nv && \
  unzip -q /tmp/mysql-connector-java.zip -d /tmp && \
  cp /tmp/mysql-connector-java-${MYSQL_CONNECTOR_JAVA_VERSION}/mysql-connector-java-${MYSQL_CONNECTOR_JAVA_VERSION}-bin.jar /apache-tomcat/lib

# PostgreSQL
RUN \
  wget https://jdbc.postgresql.org/download/postgresql-${POSTGRESQL_DRIVER_VERSION}.jar -O /tmp/postgres-driver.jar -nv && \
  cp /tmp/postgres-driver.jar /apache-tomcat/lib/

# Configure
ADD assets /assets
RUN \
  cp /assets/config/tomcat/tomcat-users.xml /apache-tomcat/conf && \
  cp -f /assets/config/explorer/engine.properties /apache-tomcat/webapps/activiti-app/WEB-INF/classes

CMD ["/bin/bash", "/assets/init"]
