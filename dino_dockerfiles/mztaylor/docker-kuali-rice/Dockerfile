# Recommended in Atlassian Speech at Dockercon
FROM phusion/baseimage:0.9.11

# File Author / Maintainer
MAINTAINER Martin Taylor

## Notes: used tomcat7 docker recipe from Maluuba as starting point

# Update the repository sources list
EXPOSE 8080

## Server setup

RUN apt-get -qq update
RUN apt-get -y install openjdk-7-jre
RUN apt-get -y install tomcat7 
RUN apt-get -y install curl

ADD start-tomcat.sh /opt/start-tomcat.sh
RUN chmod +x /opt/start-tomcat.sh


## Webapp Configuration
ENV JAVA_OPTS -Dweb.bootstrap.spring.psc=org.kuali.rice.config.KradSampleAppPSC -Dmysql.dba.url=jdbc:mysql://mysql:3306 -Dmysql.dba.username=root -Dmysql.dba.password=root

ENV Xmx 1024m

## Collect war
RUN mkdir /deployment; chmod 777 /deployment
RUN cd /deployment; curl --fail -o ROOT.war http://nexus.kuali.org/service/local/repositories/central/content/org/kuali/rice/rice-krad-sampleapp-web/2.4.1/rice-krad-sampleapp-web-2.4.1.war
RUN cd /deployment; chmod +rwx ROOT.war


## Updated libraries to run war
RUN mkdir /commonlib
RUN cd /commonlib; curl -o spring-instrument-tomcat-4.0.6.RELEASE.jar http://nexus.kuali.org/service/local/repositories/central/content/org/springframework/spring-instrument-tomcat/4.0.6.RELEASE/spring-instrument-tomcat-4.0.6.RELEASE.jar
RUN cd /commonlib; curl -o mysql-connector-java-5.1.32.jar http://nexus.kuali.org/service/local/repositories/central/content/mysql/mysql-connector-java/5.1.32/mysql-connector-java-5.1.32.jar
RUN cp /commonlib/*.jar /usr/share/tomcat7/lib/

## Add Runtime Configuration
RUN mkdir -p /usr/share/tomcat7/kuali/main/dev/rice-krad-sampleapp-web
ADD files/rice/config/rice.keystore /usr/share/tomcat7/kuali/main/dev/rice.keystore
ADD files/rice/config/common-config.xml /usr/share/tomcat7/kuali/main/dev/common-config.xml
ADD files/rice/config/krad-sampleapp-config.xml /usr/share/tomcat7/kuali/main/dev/krad-sampleapp-config.xml
ADD files/rice/config/runonce.properties /usr/share/tomcat7/kuali/main/dev/rice-krad-sampleapp-web/runonce.properties

## runonce is modified based on success/failure of process
RUN chmod 777 /usr/share/tomcat7/kuali/main/dev/rice-krad-sampleapp-web/runonce.properties

## Server Configuration

RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/logrotate

# Push war to tomcat webapp directory

ADD logrotate /etc/logrotate.d/tomcat7
RUN chmod 644 /etc/logrotate.d/tomcat7

ENTRYPOINT ["/opt/start-tomcat.sh"]
