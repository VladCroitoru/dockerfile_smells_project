FROM ubuntu:xenial

MAINTAINER Stefaan Vanderheyden <mrsvan@hotmail.com>

# Users and groups
# RUN groupadd -r tomcat && useradd -r -g tomcat tomcat
RUN echo "root:Docker!" | chpasswd

# Install packages
RUN apt-get update && \
	apt-get install -y curl unzip ssh vim net-tools git && \
	apt-get clean
	
# Export TERM as "xterm"
RUN echo -e "\nexport TERM=xterm" >> ~/.bashrc
	
# Install Java 8 JDK 
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
	apt-get clean
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV JRE_HOME=$JAVA_HOME/jre 
ENV PATH=$PATH:$JAVA_HOME/bin

# Install liferay (removing sample application "welcome-theme")
ENV LIFERAY_BASE=/opt
ENV LIFERAY_DIR=liferay-ce-portal-7.0-ga3
ENV LIFERAY_HOME=${LIFERAY_BASE}/${LIFERAY_DIR} 
ENV TOMCAT_VER=tomcat-8.0.32 
ENV TOMCAT_HOME=${LIFERAY_HOME}/${TOMCAT_VER} 
RUN cd /tmp && \
	curl -o ${LIFERAY_DIR}.zip -k -L -C - \
	"https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.0.2%20GA3/liferay-ce-portal-tomcat-7.0-ga3-20160804222206210.zip" && \
	unzip ${LIFERAY_DIR}.zip -d /opt && \
	rm ${LIFERAY_DIR}.zip && \
	rm -fr ${TOMCAT_HOME}/webapps/welcome-theme && \
	mkdir -p ${LIFERAY_HOME}/deploy && \
	mkdir -p ${LIFERAY_BASE}/script

# Add symlinks to HOME dirs
RUN ln -fs ${LIFERAY_HOME} /var/liferay && \
	ln -fs ${TOMCAT_HOME} /var/tomcat
	
# Add configuration files to liferay home
ADD conf/* ${LIFERAY_HOME}/

# Add default plugins to auto-deploy directory
ADD deploy/* ${LIFERAY_HOME}/deploy/

# Add startup scripts
ADD script/* ${LIFERAY_BASE}/script/
RUN chmod +x ${LIFERAY_BASE}/script/*.sh

# Ports
EXPOSE 8080 8443

# EXEC
CMD ["/opt/script/start.sh"]
