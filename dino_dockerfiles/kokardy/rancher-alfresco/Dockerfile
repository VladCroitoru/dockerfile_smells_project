# webcenter/rancher-alfresco

FROM ubuntu:16.04
MAINTAINER Sebastien LANGOUREAUX (linuxworkgroup@hotmail.com)

#Alfresco version
ENV ALF_URL=http://dl.alfresco.com/release/community/201612-build-00014/alfresco-community-installer-201612-linux-x64.bin
ENV ALF_HOME=/opt/alfresco


RUN mkdir -p /app/assets

# install alfresco
COPY assets/setup/install_alfresco.sh /app/assets/install_alfresco.sh
RUN chmod +x /app/assets/install_alfresco.sh
RUN /app/assets/install_alfresco.sh

# install mysql connector for alfresco
COPY assets/setup/install_mysql_connector.sh /app/assets/install_mysql_connector.sh
RUN chmod +x /app/assets/install_mysql_connector.sh
RUN /app/assets/install_mysql_connector.sh


# this is for LDAP configuration
RUN mkdir -p ${ALF_HOME}/tomcat/shared/classes/alfresco/extension/subsystems/Authentication/ldap/ldap1/
COPY assets/setup/ldap-authentication.properties ${ALF_HOME}/tomcat/shared/classes/alfresco/extension/subsystems/Authentication/ldap/ldap1/ldap-authentication.properties

# Logrotate
COPY assets/setup/logrotate-alfresco.conf /etc/logrotate.d/alfresco

# init scripts
COPY assets/init.py /app/
COPY assets/run.sh /app/
RUN chmod +x /app/*
COPY assets/setup/supervisord-alfresco.conf /etc/supervisor/conf.d/
COPY assets/setup/supervisord-postgresql.conf /etc/supervisor/conf.d/

# CLEAN APT
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV GLOBAL_PROP ${ALF_HOME}/tomcat/shared/classes/alfresco-global.properties

ENV LDAP_PROP ${ALF_HOME}/tomcat/shared/classes/alfresco/extension/subsystems/Authentication/ldap/ldap1/ldap-authentication.properties

VOLUME ["${ALF_HOME}/alf_data", GLOBAL_PROP, LDAP_PROP]

EXPOSE 21 137 138 139 445 7070 8009 8080


CMD /app/run.sh
