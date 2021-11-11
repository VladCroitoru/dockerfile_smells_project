# Liferay 6.2 CE
# 
# VERSION 0.0.2
#

FROM masieroi/docker-debian-java7

MAINTAINER Ivano Masiero <info@ivanomasiero.com>

ENV TERM=xterm

# install utils
RUN apt-get update && apt-get install -y \
nano \
zip \
vim \
unzip

# install liferay
RUN curl -O -s -k -L -C - http://downloads.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip \
	&& unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt \
	&& rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip

RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-properties=portal-postgres.properties"' >> /opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/setenv.sh

# add configuration Liferay file
ADD /portal-bundle.properties /opt/liferay-portal-6.2-ce-ga6/portal-bundle.properties
ADD /portal-postgres.properties /opt/liferay-portal-6.2-ce-ga6/portal-postgres.properties

# add Remote IDE Connector CE 2.0.1 portlet (for remote debugging)
ADD ["/portlets/server-manager-web", "/opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/webapps/server-manager-web"]

VOLUME ["/var/liferay-home", "/opt/liferay-portal-6.2-ce-ga6/"]

# Ports
EXPOSE 8080

# Set JAVA_HOME
ENV JAVA_HOME /opt/java

# EXEC
CMD ["run"]
ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/catalina.sh"]
