# Liferay 6.1
#
# VERSION 0.0.1
#

# 0.0.1 : initial file base from liferay 6.1"

FROM snasello/docker-debian-java6

MAINTAINER Samuel Nasello <samuel.nasello@elosi.com>

# install liferay
RUN apt-get install -y unzip \
	&& curl -O -s -k -L -C - http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.1.1%20GA2/liferay-portal-tomcat-6.1.1-ce-ga2-20120731132656558.zip \
	&& unzip liferay-portal-tomcat-6.1.1-ce-ga2-20120731132656558.zip -d /opt \
	&& rm liferay-portal-tomcat-6.1.1-ce-ga2-20120731132656558.zip \
	&& rm -rf /opt/liferay-portal-6.1.1-ce-ga2/tomcat-7.0.27/jre1.6.0_20 \
	&& echo '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-properties=portal-bd-${DB_TYPE}.properties"' >> /opt/liferay-portal-6.1.1-ce-ga2/tomcat-7.0.27/bin/setenv.sh

## add configuration liferay file
ADD lep/portal-bundle.properties /opt/liferay-portal-6.1.1-ce-ga2/portal-bundle.properties
ADD lep/portal-bd-MYSQL.properties /opt/liferay-portal-6.1.1-ce-ga2/portal-bd-MYSQL.properties
ADD lep/portal-bd-POSTGRESQL.properties /opt/liferay-portal-6.1.1-ce-ga2/portal-bd-POSTGRESQL.properties

# volumes
VOLUME ["/var/liferay-home", "/opt/liferay-portal-6.1.1-ce-ga2/"]

# Ports
EXPOSE 8080

# Set JAVA_HOME
ENV JAVA_HOME /opt/java

# EXEC
CMD ["run"]
ENTRYPOINT ["/opt/liferay-portal-6.1.1-ce-ga2/tomcat-7.0.27/bin/catalina.sh"]
