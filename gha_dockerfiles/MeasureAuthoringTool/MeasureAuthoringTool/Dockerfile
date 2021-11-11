FROM tomcat:10.0-jdk11-corretto

ARG STOREPASS="changeit"

RUN curl -O https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem \
    && curl -O https://s3.amazonaws.com/rds-downloads/rds-ca-2019-us-east-1.pem \
    && keytool -import -keystore $JAVA_HOME/lib/security/cacerts -trustcacerts -storepass ${STOREPASS} -alias "AWSrdsRootCACert" -file rds-ca-2019-root.pem --noprompt \
    && keytool -import -keystore $JAVA_HOME/lib/security/cacerts -trustcacerts -storepass ${STOREPASS} -alias "AWSrdsIntCACert" -file rds-ca-2019-us-east-1.pem --noprompt \
    && rm -rf /usr/local/tomcat/conf/logging.properties

RUN yum -y install unzip \
    && curl -O https://download.newrelic.com/newrelic/java-agent/newrelic-agent/current/newrelic-java.zip \
    && unzip newrelic-java.zip 

RUN mkdir /usr/local/tomcat/webapps-javaee

COPY target/MeasureAuthoringTool.war /usr/local/tomcat/webapps-javaee/
COPY context.xml /usr/local/tomcat/conf/
COPY server.xml /usr/local/tomcat/conf/

