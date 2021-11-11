# Liferay 6.2
#

# Use latest jboss/base-jdk:8 image as the base
FROM jboss/base-jdk:8

MAINTAINER Chris Boreen <cboreen@vividsolutions.com>

LABEL openshift.io.expose-services="8080:http" \
      openshift.io.tags="liferay,portal"

EXPOSE 8080

RUN curl -O -s -k -L -C - http://pilotfiber.dl.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip
RUN unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt/jboss \
	&& rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip

RUN mkdir /opt/jboss/liferay-home

# add configuration liferay file
ADD lep/portal-bundle.properties /opt/jboss/liferay-portal-6.2-ce-ga6/portal-bundle.properties
ADD lep/portal-bd-MYSQL.properties /opt/jboss/liferay-portal-6.2-ce-ga6/portal-bd-MYSQL.properties
#ADD lep/portal-bd-POSTGRESQL.properties /opt/jboss/liferay-portal-6.2-ce-ga6/portal-bd-POSTGRESQL.properties

ADD deploy/* /opt/jboss/liferay-home/deploy/
USER root
RUN chown -R jboss /opt/jboss/liferay-home
USER jboss

# add config for bdd
RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-properties=portal-bd-MYSQL.properties"' >> /opt/jboss/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/setenv.sh

# CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
CMD ["/opt/jboss/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/catalina.sh","run"]










#ADD your-awesome-app.war /opt/jboss/wildfly/standalone/deployments/
#RUN cd /opt/jboss/wildfly/standalone/deployments/ \
#    && curl -O -s -k -L -C - http://pilotfiber.dl.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-portal-6.2-ce-ga6-20160112152609836.war

#RUN cd /opt/jboss/wildfly/standalone/lib \
#    && curl -O -s -k -L -C - http://pilotfiber.dl.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-portal-dependencies-6.2-ce-ga6-20160112152609836.zip \
#    && unzip liferay-portal-dependencies-6.2-ce-ga6-20160112152609836.zip \
#    && rm liferay-portal-dependencies-6.2-ce-ga6-20160112152609836.zip



#FROM centos:centos7

#MAINTAINER Chris Boreen <cboreen@vividsolutions.com>

#LABEL k8s.io.description="Jenkins is a continuous integration server" \
#      k8s.io.display-name="Jenkins 1.651" \
#      openshift.io.expose-services="8080:http" \
#      openshift.io.tags="liferay,portal"
      
# Ports
#EXPOSE 8080

    # curl http://pkg.jenkins-ci.org/redhat/jenkins.repo -o /etc/yum.repos.d/jenkins.repo && \
    # rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key && \
#RUN yum -y --setopt=tsflags=nodocs install epel-release && \
#    INSTALL_PKGS="rsync gettext git tar zip unzip java-1.7.0-openjdk nss_wrapper" && \
#    yum -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
#    rpm -V $INSTALL_PKGS && \
#    yum clean all  && \
#    localedef -f UTF-8 -i en_US en_US.UTF-8


# install liferay
#RUN curl -O -s -k -L -C - http://pilotfiber.dl.sourceforge.net/project/lportal/Liferay%20Portal/6.2.5%20GA6/liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip \
#	&& unzip liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt \
#	&& rm liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip

#ADD liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip /opt/
#RUN unzip /opt/liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip -d /opt \
#	&& rm /opt/liferay-portal-tomcat-6.2-ce-ga6-20160112152609836.zip

# add config for bdd
#RUN /bin/echo -e '\nCATALINA_OPTS="$CATALINA_OPTS -Dexternal-properties=portal-bd-${DB_TYPE}.properties"' >> /opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/setenv.sh

# add configuration liferay file
#ADD lep/portal-bundle.properties /opt/liferay-portal-6.2-ce-ga6/portal-bundle.properties
#ADD lep/portal-bd-MYSQL.properties /opt/liferay-portal-6.2-ce-ga6/portal-bd-MYSQL.properties
#ADD lep/portal-bd-POSTGRESQL.properties /opt/liferay-portal-6.2-ce-ga6/portal-bd-POSTGRESQL.properties

#COPY ./contrib/fix-permissions /usr/local/bin
#RUN chmod 755 /usr/local/bin/fix-permissions

#RUN mkdir /var/liferay-home

# Set JAVA_HOME
# ENV JAVA_HOME /opt/java


#RUN chown -R 1001:0 /opt/liferay-portal-6.2-ce-ga6
#RUN /usr/local/bin/fix-permissions /opt/liferay-portal-6.2-ce-ga6
#RUN /usr/local/bin/fix-permissions /var/liferay-home
    
#RUN groupadd -r liferay && useradd -r -g liferay liferay
#RUN chown liferay /opt/liferay-portal-6.2-ce-ga6 -R
#RUN chown liferay /var/liferay-home -R
#RUN find /opt/liferay-portal-6.2-ce-ga6 -type d -exec chmod g+x {} +


# volumes
# VOLUME ["/var/liferay-home", "/opt/liferay-portal-6.2-ce-ga6/"]

# EXEC
#USER liferay
#CMD ["/bin/bash"]
#CMD ["run"]
#ENTRYPOINT ["/opt/liferay-portal-6.2-ce-ga6/tomcat-7.0.62/bin/catalina.sh"]
