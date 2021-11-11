FROM jboss/wildfly:10.0.0.Final

MAINTAINER Andrij David <andrijdavid@xcentrik.online>

# Download Aerogear distribution
ENV UPSVER=1.1.3.Final
ENV UPSDIST=/opt/aerogear-unifiedpush-server-$UPSVER
ENV DOMAIN=aerogear.dev

# Set MAVEN_OPTS to increase the amount of memory available for Maven

ENV MAVEN_OPTS -Xmx768m -XX:+UseConcMarkSweepGC -XX:MaxPermSize=128m -XX:+CMSClassUnloadingEnabled

# ENV variable
RUN export DOMAIN=$DOMAIN

USER root

# Clean the metadata
# install openssl needed for certificate
RUN yum update -y \
	&& yum install -y unzip wget openssl \
	&& yum -q clean all

## MYSQL
ENV mysql_module_dir=$JBOSS_HOME/modules/com/mysql/jdbc/main/
RUN mkdir -p ${mysql_module_dir}
RUN wget -O mysql-connector-java-5.1.18.jar http://search.maven.org/remotecontent\?filepath\=mysql/mysql-connector-java/5.1.18/mysql-connector-java-5.1.18.jar
RUN mv mysql-connector-java-5.1.18.jar ${mysql_module_dir}
COPY configuration/xml/mysql-module.xml ${mysql_module_dir}/module.xml

# Rename the original configuration file
RUN mv $JBOSS_HOME/standalone/configuration/standalone.xml $JBOSS_HOME/standalone/configuration/standalone.xml.orig

# WildFly configuration file ready for HTTPS
ADD configuration/xml/standalone-full-sample.xml $JBOSS_HOME/standalone/configuration/standalone.xml

# Add the certificate.sh script into $JBOSS_HOME/standalone/configuration/certs
ADD configuration/certs/ $JBOSS_HOME/standalone/configuration/certs

# update rights for everything to be jboss user owned
RUN chown -R jboss:jboss $JBOSS_HOME/standalone

# Switch to $JBOSS_HOME/configuration/certs
WORKDIR /opt/jboss/wildfly/standalone/configuration/certs

# Execute the script to generate self signed certificates
RUN ./certificate.sh

# Switch to the working dir /opt/jboss/wildfly
WORKDIR /opt/jboss/wildfly

RUN curl -L -o /opt/aerogear-unifiedpush-server-$UPSVER-dist.tar.gz https://github.com/aerogear/aerogear-unifiedpush-server/releases/download/$UPSVER/aerogear-unifiedpush-server-$UPSVER-dist.tar.gz
WORKDIR /opt
RUN tar zxf aerogear-unifiedpush-server-$UPSVER-dist.tar.gz

# unzip migrator and copy liquibase.properties
WORKDIR $UPSDIST/migrator
RUN unzip ups-migrator-dist.zip
COPY configuration/liquibase.properties  $UPSDIST/migrator/ups-migrator/

# Run everything below as aerogear user
USER jboss

# Switch to the working dir $JBOSS_HOME/standalone/deployments
WORKDIR /opt/jboss/wildfly/standalone/deployments

# copy war files
RUN   cp $UPSDIST/servers/unifiedpush-auth-server.war $JBOSS_HOME/standalone/deployments \
      && cp $UPSDIST/servers/unifiedpush-server-wildfly.war $JBOSS_HOME/standalone/deployments

# Expose SSL default port
EXPOSE 8443

# copy and run startup script
# migration is done inside the startup script before launching the server
COPY entrypoint.sh /opt/
ENTRYPOINT ["/opt/entrypoint.sh"]