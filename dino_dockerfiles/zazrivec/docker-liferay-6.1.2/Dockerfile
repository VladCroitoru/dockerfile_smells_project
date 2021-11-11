# Liferay 6.1.2
#
# VERSION 0.0.7
#

# 0.0.1 : initial file with java 7u60
# 0.0.2 : change base image : java 7u71
# 0.0.3 : chain run commande to reduce image size (from 1.175 GB to 883.5MB), add JAVA_HOME env
# 0.0.4 : change to debian:wheezy in order to reduce image size (883.5MB -> 664.1 MB)
# 0.0.5 : bug with echo on setenv.sh
# 0.0.6 : liferay 6.2-ce-ga3 + java 7u79
# 0.0.7 : liferay 6.2-ce-ga4

FROM snasello/docker-debian-java7:7u79

MAINTAINER Samuel Nasello <samuel.nasello@elosi.com>

# install liferay
RUN curl -O -s -k -L -C - http://sourceforge.net/projects/lportal/files/Liferay%20Portal/6.1.2%20GA3/liferay-portal-tomcat-6.1.2-ce-ga3-20130816114619181.zip \
	&& unzip liferay-portal-tomcat-6.1.2-ce-ga3-20130816114619181.zip -d /opt \
	&& rm liferay-portal-tomcat-6.1.2-ce-ga3-20130816114619181.zip

# add config for bdd
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-properties=portal-bd-${DB_TYPE}.properties"' >> /opt/liferay-portal-6.1.2-ce-ga3/tomcat-7.0.40/bin/setenv.sh

# add configuration liferay file
ADD lep/portal-bundle.properties /opt/liferay-portal-6.1.2-ce-ga3/portal-bundle.properties
ADD lep/portal-bd-MYSQL.properties /opt/liferay-portal-6.1.2-ce-ga3/portal-bd-MYSQL.properties
ADD lep/portal-bd-POSTGRESQL.properties /opt/liferay-portal-6.1.2-ce-ga3/portal-bd-POSTGRESQL.properties
ADD lep/portal-bd-POSTGRESQL2.properties /opt/liferay-portal-6.1.2-ce-ga3/portal-bd-POSTGRESQL2.properties

# volumes
VOLUME ["/var/liferay-home", "/opt/liferay-portal-6.1.2-ce-ga3/"]

# Ports
EXPOSE 8080

# Set JAVA_HOME
ENV JAVA_HOME /opt/java

# EXEC
CMD ["run"]
ENTRYPOINT ["/opt/liferay-portal-6.1.2-ce-ga3/tomcat-7.0.40/bin/catalina.sh"]
