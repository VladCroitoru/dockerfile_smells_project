FROM tomcat:7
MAINTAINER Neil Carpenter <neil@twistlock.com>
ARG struts2_version=2.3.12
RUN apt-get update
RUN apt-get -y install curl git nmap dnsutils 
RUN set -ex \
	&& rm -rf /usr/local/tomcat/webapps/* \
	&& chmod a+x /usr/local/tomcat/bin/*.sh
RUN curl -o /usr/local/tomcat/webapps/ROOT.war http://central.maven.org/maven2/org/apache/struts/struts2-showcase/${struts2_version}/struts2-showcase-${struts2_version}.war
EXPOSE 8080
