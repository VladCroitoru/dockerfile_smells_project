FROM ubuntu:xenial

# install software
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		openjdk-8-jre \
		tomcat7 \
		unzip \
		curl \
	&& rm -rf /var/lib/apt/lists/*

# prepare tomcat environment
RUN mkdir -p /usr/share/tomcat7/lib \
	&& mkdir -p /usr/share/tomcat7/conf \
	&& mkdir -p /usr/share/tomcat7/conf/Catalina/localhost \
	&& cp -R /var/lib/tomcat7/conf/* /usr/share/tomcat7/conf/ \
	&& ln -s /tmp /usr/share/tomcat7/temp
	
# replace tomcat configuration
COPY docker/server.xml /usr/share/tomcat7/conf/
COPY TomCatConfig/context.xml /usr/share/tomcat7/conf/

# download and unpack flamingo
RUN curl "http://central.maven.org/maven2/com/sun/mail/javax.mail/1.5.2/javax.mail-1.5.2.jar" > /usr/share/tomcat7/lib/javax.mail-1.5.2.jar \
	&& curl "http://central.maven.org/maven2/postgresql/postgresql/9.0-801.jdbc4/postgresql-9.0-801.jdbc4.jar" > /usr/share/tomcat7/lib/postgresql-9.0-801.jdbc4.jar \
	&& mkdir -p /usr/share/tomcat7/webapps/ \
	&& curl "http://nexus.idgis.eu/content/repositories/releases/nl/idgis/sys/provisioning-registration-war/1.1.5/provisioning-registration-war-1.1.5.war" > /usr/share/tomcat7/webapps/provisioning-registration-war.war \
	&& curl "http://repo.b3p.nl/nexus/content/repositories/releases/org/flamingo-mc/viewer/4.6.4/viewer-4.6.4.war" > /usr/share/tomcat7/webapps/viewer.war \
	&& curl "http://repo.b3p.nl/nexus/content/repositories/releases/org/flamingo-mc/viewer-admin/4.6.4/viewer-admin-4.6.4.war" > /usr/share/tomcat7/webapps/viewer-admin.war \
	&& unzip -d /usr/share/tomcat7/webapps/provisioning-registration-war /usr/share/tomcat7/webapps/provisioning-registration-war.war \
	&& unzip -d /usr/share/tomcat7/webapps/viewer /usr/share/tomcat7/webapps/viewer.war \
	&& unzip -d /usr/share/tomcat7/webapps/viewer-admin /usr/share/tomcat7/webapps/viewer-admin.war \
	&& rm /usr/share/tomcat7/webapps/provisioning-registration-war.war \
	&& rm /usr/share/tomcat7/webapps/viewer.war \
	&& rm /usr/share/tomcat7/webapps/viewer-admin.war
	
COPY viewer/src/main/webapp/idgis/components /usr/share/tomcat7/webapps/viewer/idgis/components

EXPOSE 8080 8009

# default environment
ENV ZOOKEEPER_HOSTS="zookeeper" \
	SERVICE_IDENTIFICATION="flamingo" \
	SERVICE_DOMAIN="localhost" \
	SERVICE_AJP_PORT="8009" \
	SERVICE_HTTP_PORT="8080" \
	SERVICE_PATH="/"
	
COPY docker/start.sh /opt/

# set permisions
RUN chown -R tomcat7:tomcat7 /usr/share/tomcat7/ \
	&& chmod a+x /opt/start.sh

USER tomcat7
CMD ["/opt/start.sh"]
