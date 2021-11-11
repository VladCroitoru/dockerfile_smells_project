FROM jboss/base-jdk:8
MAINTAINER john@kanej.me

# Setup keycloak
ENV KEYCLOAK_VERSION 1.1.0.Final
RUN cd $HOME; curl -O http://central.maven.org/maven2/org/keycloak/keycloak-appliance-dist-all/$KEYCLOAK_VERSION/keycloak-appliance-dist-all-$KEYCLOAK_VERSION.zip; unzip keycloak-appliance-dist-all-$KEYCLOAK_VERSION.zip; mv $HOME/keycloak-appliance-dist-all-$KEYCLOAK_VERSION/keycloak $HOME/keycloak; rm -rf $HOME/keycloak-appliance-dist-all-$KEYCLOAK_VERSION.zip; rm -rf $HOME/keycloak-appliance-dist-all-$KEYCLOAK_VERSION
ENV JBOSS_HOME /opt/jboss/keycloak
EXPOSE 8080
EXPOSE 8443
CMD ["/opt/jboss/keycloak/bin/standalone.sh", "-b", "0.0.0.0"]

# Setup up postgres as the backend database
ADD changeDatabase.xsl /opt/jboss/keycloak/
RUN java -jar /usr/share/java/saxon.jar -s:/opt/jboss/keycloak/standalone/configuration/standalone.xml -xsl:/opt/jboss/keycloak/changeDatabase.xsl -o:/opt/jboss/keycloak/standalone/configuration/standalone.xml
RUN mkdir -p /opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; cd /opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main; curl -O http://central.maven.org/maven2/org/postgresql/postgresql/9.3-1102-jdbc3/postgresql-9.3-1102-jdbc3.jar
ADD module.xml /opt/jboss/keycloak/modules/system/layers/base/org/postgresql/jdbc/main/

VOLUME ["/opt/jboss/keycloak/standalone/deployments"]
VOLUME ["/opt/jboss/keycloak/standalone/configuration/security"]

# Setup HTTPS on wildfly
ADD setupHttps.xsl /opt/jboss/keycloak/
RUN java -jar /usr/share/java/saxon.jar -s:/opt/jboss/keycloak/standalone/configuration/standalone.xml -xsl:/opt/jboss/keycloak/setupHttps.xsl -o:/opt/jboss/keycloak/standalone/configuration/standalone.xml
RUN sed -i s/KEYSTORE_PASSWORD/\$\{env\.KEYSTORE_PASSWORD\:password\}/ /opt/jboss/keycloak/standalone/configuration/standalone.xml
ENV KEYSTORE_PASSWORD password

# Import the realm from the security folder.
RUN echo 'JAVA_OPTS="$JAVA_OPTS -Dkeycloak.import=/opt/jboss/keycloak/standalone/configuration/security/realm.json"' >> /opt/jboss/keycloak/bin/standalone.conf
